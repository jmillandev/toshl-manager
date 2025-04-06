class RoomieExpensesCleaner:

    @classmethod
    def clean(cls, data):
        response = []
        sum = 0
        for row in data:
            amount = abs(row["amount"])
            response.append(
                {
                    "Description": row["desc"].replace("\n", " - "),
                    "USD Amount": str(amount),
                    "Category": cls._format_category(row),
                    "Tags": cls._format_tags(row),
                    "Date": row["date"],
                    "ID": row["id"],
                }
            )
            sum += amount

        response.append(
            {
                "Description": "TOTAL * 42.37%",
                "USD Amount": f"{sum * 0.4237 :.3f}",
                "Category": "---",
                "Tags": "---",
                "Date": "---",
                "ID": "---",
            }
        )
        return response

    @classmethod
    def _format_category(cls, row):
        categories = row["included"].get("category")
        if not categories:
            return row["category"]

        return categories[row["category"]]["name"]

    @classmethod
    def _format_tags(cls, row):
        tags = row["included"].get("tags")
        if not tags:
            return " - ".join(row["tags"])

        return " - ".join(map(lambda tg: tags[tg]["name"], row["tags"]))
