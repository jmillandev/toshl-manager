from config import SEPARATOR


class RoomieExpensesFormatter:

    @staticmethod
    def format(data):
        response = []
        sum = 0
        for row in data:
            amount = abs(row["amount"])
            response.append(
                {
                    "Description": row["desc"].replace('\n', ' - '),
                    "USD Amount": str(amount),
                    "Category": row["category"],
                    "Tags": SEPARATOR.join(row["tags"]),
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
