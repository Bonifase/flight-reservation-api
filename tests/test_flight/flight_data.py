new_flight = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")
another_flight = dict(
                name="Boeng",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")
duplicate_name = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")

missing_name = dict(
                name="",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")

missing_departure = dict(
                name="Flight No 3",
                departure="",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")

missing_arrival = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                arrival="",
                destination="Dallas")

missing_destination = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="")

invalid_name = dict(
                name="#$#",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")

invalid_destination = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="#@#")

missing_name_key = dict(
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")

missing_departure_key = dict(
                name="Flight No 3",
                arrival="2015-05-12 13:30:00+00",
                destination="Dallas")

missing_arrival_key = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                destination="Dallas")

missing_destination_key = dict(
                name="Flight No 3",
                departure="2015-05-12 13:30:00+00",
                arrival="2015-05-12 13:30:00+00")

update_flight = dict(
                name="Flight No 1",
                departure="2015-05-12 14:30:00+00",
                arrival="2015-05-12 23:30:00+00",
                destination="Dallas")

new_seat = dict(number=1)

missing_number = dict(number="")

invalid_number = dict(number="$$$")

number_key_missing = dict()
