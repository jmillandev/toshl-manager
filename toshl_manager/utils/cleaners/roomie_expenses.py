class RoomieExpensesCleaner:

    @staticmethod
    def clean(data):
        response = []
        sum = 0
        for row in data:
            amount = abs(row["amount"])
            categories = row["included"]["category"]
            tags = row["included"]["tags"]
            response.append(
                {
                    "Description": row["desc"].replace('\n', ' - '),
                    "USD Amount": str(amount),
                    "Category": categories[row["category"]]["name"],
                    "Tags": " - ".join(map(lambda tg: tags[tg]["name"], row["tags"])),
                    "Date": row["date"],
                    "ID": row["id"],
                }
            )
            sum += amount

        response.append(
            {
                "Description": "TOTAL / 2",
                "USD Amount": f"{sum/2:.3f}",
                "Category": "---",
                "Tags": "---",
                "Date": "---",
                "ID": "---",
            }
        )
        return response
