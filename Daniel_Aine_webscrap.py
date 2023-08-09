import requests, csv, json

def fetch_bird_songs():
    url = 'https://xeno-canto.org/api/2/recordings'
    query = 'type:song'  # Add the query parameter to fetch bird songs only
    params = {'query': query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        bird_songs_list = []

        for bird in data['recordings']:
            bird_species = bird['en']
            bird_group = bird['group']
            bird_file_url = bird['file']
            bird_file_name = bird['file-name']
            bird_sex = bird.get('sex', 'Unknown')
            bird_time = bird.get('time', 'Unknown')
            bird_date = bird.get('date', 'Unknown')
            bird_country = bird.get('cnt', 'Unknown')
            bird_url = bird.get('url', 'Unknown')
            bird_method = bird.get('method', 'Unknown')

            bird_data = {
                'species': bird_species,
                'group': bird_group,
                'file_url': bird_file_url,
                'file_name': bird_file_name,
                'sex': bird_sex,
                'time': bird_time,
                'date': bird_date,
                'country': bird_country,
                'url': bird_url,
                'method': bird_method,
                # Add other attributes as needed
            }
            bird_songs_list.append(bird_data)

        return bird_songs_list
    else:
        print('Failed to fetch data from the API.')
        return None

def save_to_csv(data, file_name):
    fields = ['species', 'group', 'file_url', 'file_name', 'sex', 'time', 'date', 'country', 'url', 'method']

    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    # Fetch bird songs data
    bird_songs_data = fetch_bird_songs()

    if bird_songs_data:
        # Save data to CSV file
        save_to_csv(bird_songs_data, 'bird_info.csv')

        # Save data to JSON file
        save_to_json(bird_songs_data, 'bird_info.json')

        print('Data successfully extracted and saved to CSV and JSON files.')
    else:
        print('Failed to fetch data. Check the URL or API availability.')
