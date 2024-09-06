athletes = []
events = []
medal_count = {} 

def add_details():
    athletes_record = int(input("How many athletes do you want to add? "))
    
    for _ in range(athletes_record):
        athlete_name = input("Enter athlete name: ")
        year = int(input("Enter Event year: "))
        country = input("Enter athlete's country: ")
        event_name = input("Enter event name: ")
        performance = input("Enter performance metrics (e.g., time, distance): ")
        medal = input("Enter medal won (Gold/Silver/Bronze/None): ")

        athlete_record = {
            "name": athlete_name,
            "year": year,
            "country": country,
            "event": event_name,
            "performance": performance,
            "medal": medal
        }
        athletes.append(athlete_record)

        event_record = {
            "event": event_name,
            "athlete": athlete_name,
            "performance": performance,
            "medal": medal,
            "year": year,
            "country": country
        }
        events.append(event_record)

        if medal != "None":
            if country in medal_count:
                medal_count[country][medal] += 1
            else:
                medal_count[country] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                medal_count[country][medal] += 1

def view_details():
    event_name = input("Enter event name to view details: ")
    print(f"\nDetails for event: {event_name}")
    header = f"{'Athlete':<20}{'Performance':<20}{'Medal':<10}{'Year':<10}{'Country':<15}"
    print(header)
    print("=" * 75)

    for event in events:
        if event['event'] == event_name:
            row = f"{event['athlete']:<20}{event['performance']:<20}{event['medal']:<10}{event['year']:<10}{event['country']:<15}"
            print(row)

def view_medal_count():
    print("\nMedal Count by Country:")
    header = f"{'Country':<20}{'Gold':<10}{'Silver':<10}{'Bronze':<10}"
    print(header)
    print("=" * 50)

    for country, medals in medal_count.items():
        row = f"{country:<20}{medals['Gold']:<10}{medals['Silver']:<10}{medals['Bronze']:<10}"
        print(row)

def search_athlete_performance():
    athlete_name = input("Enter athlete name to search performance: ")
    print(f"\nPerformance of {athlete_name}:")
    header = f"{'Event':<20}{'Performance':<20}{'Medal':<10}{'Year':<10}{'Country':<15}"
    print(header)
    print("=" * 50)
    

    for athlete in athletes:
        if athlete['name'] == athlete_name:
            row = f"{athlete['event']:<20}{athlete['performance']:<20}{athlete['medal']:<10}{athlete['year']:<10}{athlete['country']:<15}"
            print(row)

def view_event_details():
    view_details()

def view_statistics():
    total_events = len(events)
    total_athletes = len(athletes)
    print("\nStatistics:")
    print(f"Total events: {total_events}")
    print(f"Total athletes: {total_athletes}")
    print(f"Average number of athletes per event: {total_athletes / total_events if total_events > 0 else 0}")

def main():
    while True:
        print("1. Add Details")
        print("2. View Details")
        print("3. View Medal Count by Country")
        print("4. Search Athlete Performance")
        print("5. View Event Details")
        print("6. View Statistics") 
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_details()
        elif choice == '2':
            view_details()
        elif choice == '3':
            view_medal_count()
        elif choice == '4':
            search_athlete_performance()
        elif choice == '5':
            view_event_details()
        elif choice == '6':
            view_statistics()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
