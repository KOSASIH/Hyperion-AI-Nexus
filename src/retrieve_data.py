import requests
import markdown

def retrieve_data():
    # Retrieve data from the database or API
    response = requests.get('https://api.example.com/ai-professionals')
    data = response.json()
    return data

def generate_markdown_table(data):
    # Generate the markdown table
    table = "| Name | Affiliation | Contact Details |\n"
    table += "| --- | --- | --- |\n"
    
    for entry in data:
        name = entry['name']
        affiliation = entry['affiliation']
        contact_details = entry['contact_details']
        table += f"| {name} | {affiliation} | {contact_details} |\n"
    
    return table

def main():
    # Retrieve data
    data = retrieve_data()
    
    # Generate markdown table
    table = generate_markdown_table(data)
    
    # Display the formatted markdown table
    print(markdown.markdown(table))

if __name__ == '__main__':
    main()
