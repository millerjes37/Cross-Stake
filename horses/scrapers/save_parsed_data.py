import json
from horses.models import Race, FeeSchedule

def save_parsed_data(json_string):
    data = json.loads(json_string)
    
    for race_data in data['races']:
        race, created = Race.objects.get_or_create(
            name=race_data['name'],
            date=race_data['date'],
            location=race_data['location']
        )

        for fee_schedule_data in race_data['fee_schedules']:
            FeeSchedule.objects.create(
                race=race,
                date=fee_schedule_data['date'],
                entrance_fee=fee_schedule_data['entrance_fee'],
                registration_fee=fee_schedule_data['registration_fee'],
                staking_fee=fee_schedule_data['staking_fee']
            )

if __name__ == "__main__":
    json_string = '...'  # The JSON string from either OpenAI or Claude
    save_parsed_data(json_string)
