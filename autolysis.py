import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import uuid

# Helper Functions
def validate_inputs():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    csv_filename = sys.argv[1]
    if not os.path.isfile(csv_filename):
        print(f"Error: File {csv_filename} does not exist.")
        sys.exit(1)

    return csv_filename


def load_dataset(csv_filename):
    try:
        return pd.read_csv(csv_filename)
    except Exception as e:
        print(f"Error reading {csv_filename}: {e}")
        sys.exit(1)


def analyze_data(data):
    # Summarize data
    summary = data.describe(include="all").to_dict()
    missing_values = data.isnull().sum().to_dict()
    correlations = data.corr().to_dict()

    return {
        "summary": summary,
        "missing_values": missing_values,
        "correlations": correlations,
    }


def generate_visualizations(data):
    output_files = []

    # Correlation Heatmap
    if not data.corr().empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        heatmap_file = f"heatmap_{uuid.uuid4().hex[:8]}.png"
        plt.savefig(heatmap_file)
        output_files.append(heatmap_file)
        plt.close()

    # Numerical Data Distribution
    for column in data.select_dtypes(include=["number"]).columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column].dropna(), kde=True, bins=30)
        dist_file = f"dist_{column}_{uuid.uuid4().hex[:8]}.png"
        plt.savefig(dist_file)
        output_files.append(dist_file)
        plt.close()

    return output_files


def query_llm(prompt):
    openai.api_key = os.getenv("AIPROXY_TOKEN")
    if not openai.api_key:
        print("Error: AIPROXY_TOKEN environment variable is not set.")
        sys.exit(1)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error querying GPT-4o-Mini: {e}")
        sys.exit(1)


def generate_story(analysis, visualizations):
    prompt = f"""
    Analyze the following dataset:
    Summary Statistics: {analysis['summary']}
    Missing Values: {analysis['missing_values']}
    Correlation Matrix: {analysis['correlations']}
    Visualizations: {', '.join(visualizations)}

    Write a concise narrative describing:
    - The dataset and key statistics.
    - Insights from the analysis.
    - Recommendations or actions based on the findings.
    """
    return query_llm(prompt)


def save_results(readme_content, visualizations, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Save README.md
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content)

    # Move visualization files to output directory
    for vis in visualizations:
        os.rename(vis, os.path.join(output_dir, os.path.basename(vis)))


# Main Script
def main():
    csv_filename = validate_inputs()
    data = load_dataset(csv_filename)

    analysis = analyze_data(data)
    visualizations = generate_visualizations(data)
    narrative = generate_story(analysis, visualizations)

    # Combine results into README.md content
    readme_content = f"# Analysis Report\n\n## Narrative\n\n{narrative}\n\n## Visualizations\n\n"
    for vis in visualizations:
        readme_content += f"![{vis}]({os.path.basename(vis)})\n\n"

    # Save results
    output_dir = os.path.splitext(csv_filename)[0]
    save_results(readme_content, visualizations, output_dir)
    print(f"Analysis complete. Results saved in '{output_dir}'.")


if __name__ == "__main__":
    main()
