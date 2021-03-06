class LoansCleaner:

    @staticmethod
    def clean(data):
        response = []
        sum = 0
        for row in data:
            amount = abs(row["amount"])
            response.append(
                {
                    "Description": row["desc"].replace('\n', ' - '),
                    "USD Amount": amount,
                    "Date": row["date"],
                    "ID": row["id"],
                }
            )
            sum += amount

        response.append(
            {
                "Description": "TOTAL",
                "USD Amount": sum,
                "Date": "---",
                "ID": "---",
            }
        )
        return response
