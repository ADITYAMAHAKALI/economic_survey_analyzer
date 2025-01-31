import json
import re
from pathlib import Path

# Path to the JSON data file
json_file = Path("./economic_survey_summaries.json")

# Path to the output HTML file
output_html = Path("economic_survey_2025_summary.html")

# Function to generate a URL-friendly ID from file_name
def generate_id(file_name):
    # Convert to lowercase
    id_str = file_name.lower()
    # Replace spaces and underscores with hyphens
    id_str = re.sub(r'[\s_]+', '-', id_str)
    # Remove any characters that are not alphanumeric or hyphens
    id_str = re.sub(r'[^a-z0-9\-]', '', id_str)
    return id_str

# Read JSON data
try:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: {json_file} not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Collect file names and generate their IDs for the index
index_entries = []
for item in data:
    raw_file_name = item.get("file_name", "N/A").replace("_", " ")
    file_name = raw_file_name.strip().upper()
    summary_id = generate_id(file_name)
    index_entries.append({"file_name": file_name, "id": summary_id})

# Start building the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Economic Survey 2025 Summary Report</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Montserrat:wght@600&display=swap" rel="stylesheet">
    <style>
        /* Global Styles */
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #FFFFFF; /* White Background */
            color: #333333; /* Dark Text for Readability */
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #FF671F; /* Saffron */
            color: #FFFFFF;
            padding: 30px 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        header h1 {
            margin: 0;
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5em;
        }
        .container {
            padding: 40px 20px;
            max-width: 1200px;
            margin: auto;
        }
        /* Index (Table of Contents) Styles */
        .index {
            background-color: #F9F9F9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 40px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .index h2 {
            color: #FF671F; /* Saffron */
            font-family: 'Montserrat', sans-serif;
            margin-bottom: 15px;
            font-size: 1.5em;
            border-bottom: 2px solid #FF671F;
            padding-bottom: 10px;
        }
        .index ul {
            list-style-type: none;
            padding-left: 0;
        }
        .index li {
            margin-bottom: 10px;
        }
        .index a {
            color: #046A38; /* Green */
            text-decoration: none;
            font-size: 1.1em;
            transition: color 0.3s;
        }
        .index a:hover {
            color: #06038D; /* Navy Blue */
            text-decoration: underline;
        }
        .summary {
            background-color: #FDFDFD;
            margin-bottom: 30px;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            transition: box-shadow 0.3s;
        }
        .summary:hover {
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .summary h2 {
            color: #FF671F; /* Saffron */
            font-family: 'Montserrat', sans-serif;
            margin-bottom: 10px;
            font-size: 1.8em;
            border-bottom: 2px solid #FF671F;
            padding-bottom: 10px;
        }
        .summary p {
            line-height: 1.8;
            color: #555555;
            margin-bottom: 15px;
        }
        .summary .section {
            margin-bottom: 20px;
        }
        .summary .section h3 {
            color: #046A38; /* Green */
            font-family: 'Montserrat', sans-serif;
            margin-bottom: 8px;
            font-size: 1.2em;
            border-left: 4px solid #046A38;
            padding-left: 10px;
        }
        footer {
            background-color: #06038D; /* Navy Blue */
            color: #FFFFFF;
            text-align: center;
            padding: 20px;
            position: relative;
            bottom: 0;
            width: 100%;
            box-shadow: 0 -2px 4px rgba(0,0,0,0.1);
        }
        footer p {
            margin: 0;
            font-size: 0.9em;
        }
        /* Responsive Design */
        @media (max-width: 768px) {
            .container {
                padding: 20px 10px;
            }
            header h1 {
                font-size: 2em;
            }
            .index {
                padding: 15px;
            }
            .index h2 {
                font-size: 1.3em;
            }
            .index a {
                font-size: 1em;
            }
            .summary {
                padding: 20px;
            }
            .summary h2 {
                font-size: 1.5em;
            }
            .summary .section h3 {
                font-size: 1em;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Economic Survey 2025 Summary Report</h1>
    </header>
    <div class="container">
        <!-- Linked Index (Table of Contents) -->
        <div class="index">
            <h2>Table of Contents</h2>
            <ul>
"""

# Generate the index list items with links
for entry in index_entries:
    file_name = entry["file_name"]
    summary_id = entry["id"]
    html_content += f'                <li><a href="#{summary_id}">{file_name}</a></li>\n'

# Close the index div
html_content += """            </ul>
        </div>
"""

# Iterate through each summary object and add to HTML with unique IDs
for item in data:
    raw_file_name = item.get("file_name", "N/A").replace("_", " ")
    file_name = raw_file_name.strip().upper()
    summary_id = generate_id(file_name)
    # text_length = item.get("text_length", 0)  # Uncomment if you want to include text_length in the HTML
    summary = item.get("summary", {})

    html_content += f"""
        <div class="summary" id="{summary_id}">
            <h2>{file_name}</h2>
    """

    # Iterate through each section in the summary
    for section_title, section_content in summary.items():
        # Replace underscores with spaces and add proper casing
        formatted_title = section_title.replace("_", " ")
        html_content += f"""
            <div class="section">
                <h3>{formatted_title}</h3>
                <p>{section_content}</p>
            </div>
        """

    html_content += "</div>\n"

# Close the container and add footer
html_content += """
    </div>
    <footer>
        <p>&copy; 2025 Economic Survey. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Write the HTML content to the output file
try:
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML report successfully saved to {output_html}")
except IOError as e:
    print(f"Error writing to {output_html}: {e}")
