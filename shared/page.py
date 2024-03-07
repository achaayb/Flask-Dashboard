
class Page:
    def __init__(self, rows=list(), page=1, per_page=10, total_rows=0):
        
        self.data = rows

        page = max(1, page)

        total_records = len(self.data)
        total_pages = (total_rows + per_page - 1) // per_page

        self.pagination = {
            "total_records": total_records,
            "current_page": page,
            "total_pages": total_pages,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
        }