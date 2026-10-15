"""
Flight Reservation System
Data Structures: Searching and Sorting
Language: Python 3
Note: Demonstration program using in-memory sample data; it does not connect to a real airline.
"""

flights = [
    {"flight_no": "AI101", "source": "Pune", "destination": "Delhi", "departure": "08:30", "price": 5200, "seats": 20},
    {"flight_no": "6E204", "source": "Pune", "destination": "Bengaluru", "departure": "10:15", "price": 3800, "seats": 15},
    {"flight_no": "UK812", "source": "Mumbai", "destination": "Delhi", "departure": "14:00", "price": 6100, "seats": 12},
    {"flight_no": "AI305", "source": "Pune", "destination": "Hyderabad", "departure": "17:45", "price": 4200, "seats": 18},
]

reservations = []
next_booking_id = 1001


def display_flights(records):
    if not records:
        print("No matching flights found.")
        return
    print(f"{'Flight':<10}{'From':<14}{'To':<14}{'Departure':<12}{'Price':>8}{'Seats':>8}")
    print("-" * 66)
    for f in records:
        print(f"{f['flight_no']:<10}{f['source']:<14}{f['destination']:<14}"
              f"{f['departure']:<12}{f['price']:>8}{f['seats']:>8}")


def linear_search_flight(flight_no):
    """Linear search: O(n) time."""
    target = flight_no.strip().upper()
    for flight in flights:
        if flight["flight_no"].upper() == target:
            return flight
    return None


def binary_search_by_price(sorted_flights, target_price):
    """Binary search requires records sorted by price; O(log n) time."""
    low, high = 0, len(sorted_flights) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_flights[mid]["price"] == target_price:
            return sorted_flights[mid]
        if sorted_flights[mid]["price"] < target_price:
            low = mid + 1
        else:
            high = mid - 1
    return None


def sort_flights(key="price"):
    """Return a new list sorted by a supported field."""
    if key not in {"price", "departure", "flight_no"}:
        raise ValueError("Unsupported sort field.")
    return sorted(flights, key=lambda f: f[key])


def book_flight(flight_no, passenger_name):
    global next_booking_id
    flight = linear_search_flight(flight_no)
    if flight is None:
        print("Booking failed: flight not found.")
        return None
    if flight["seats"] <= 0:
        print("Booking failed: no seats available.")
        return None
    flight["seats"] -= 1
    booking = {
        "booking_id": next_booking_id,
        "passenger": passenger_name.strip(),
        "flight_no": flight["flight_no"],
    }
    next_booking_id += 1
    reservations.append(booking)
    print(f"Booking confirmed. Booking ID: {booking['booking_id']}")
    return booking


def cancel_booking(booking_id):
    for i, booking in enumerate(reservations):
        if booking["booking_id"] == booking_id:
            flight = linear_search_flight(booking["flight_no"])
            if flight:
                flight["seats"] += 1
            reservations.pop(i)
            print("Booking cancelled.")
            return True
    print("Booking ID not found.")
    return False


def main():
    while True:
        print("\n=== FLIGHT RESERVATION SYSTEM ===")
        print("1. Display all flights")
        print("2. Search by flight number (linear search)")
        print("3. Sort flights by price")
        print("4. Sort flights by departure time")
        print("5. Binary search by exact price (after sorting)")
        print("6. Book a flight")
        print("7. Cancel a booking")
        print("8. View reservations")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_flights(flights)
        elif choice == "2":
            result = linear_search_flight(input("Flight number: "))
            display_flights([result] if result else [])
        elif choice == "3":
            display_flights(sort_flights("price"))
        elif choice == "4":
            display_flights(sort_flights("departure"))
        elif choice == "5":
            sorted_records = sort_flights("price")
            price_text = input("Exact price to search: ").strip()
            if price_text.isdigit():
                result = binary_search_by_price(sorted_records, int(price_text))
                display_flights([result] if result else [])
            else:
                print("Enter a whole-number price.")
        elif choice == "6":
            book_flight(input("Flight number: "), input("Passenger name: "))
        elif choice == "7":
            booking_text = input("Booking ID: ").strip()
            if booking_text.isdigit():
                cancel_booking(int(booking_text))
            else:
                print("Invalid booking ID.")
        elif choice == "8":
            if not reservations:
                print("No reservations yet.")
            else:
                for r in reservations:
                    print(r)
        elif choice == "0":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
