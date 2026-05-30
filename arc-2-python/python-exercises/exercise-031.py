#Challenge 031 - Create a program that asks a trip distance in Km. Calculate the ticket price, charging R$0,50 per Km for trips up to 200km and R$0,45 for longer trips.

print("=" * 10, "[Challenge 031]", "=" * 10)
trip_distance = float(input("Trip Distance: "))
if trip_distance <= 200:
    ticket_price = trip_distance * 0.50
else:
    ticket_price = trip_distance * 0.45
print("=" * 30, f"\nTicket Price: R${ticket_price:.2f}\n", "=" * 30)