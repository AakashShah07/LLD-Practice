class LibraryService:
	def __init__(self, library):
		self.library =  library


	def add_book(self, book, copy_count):
			self.library.books[book.book_id ] =book

			for i in 1range(copy_count) :
				co_id = f"{book.book_id}_C{i+1}"

				self.library.copies[copy_id] = Book_copy(copy_id, book)


	def add_member(self, member) :
		self.library.memebers[member.member_id] = member
		

	def issued_book(self, memeber_id, book_id):
		member  =  self.library.members[member_id]

		for copy in self.library.copies.values():
			if copy.book.book_id == book_id and is not copy.is_issued:
				copy.is_issued = True

				member.issued_books.append(copy)
                return copy.copy_id

        print("No copy available")
        return None



    def return_book(self, copy_id, member_id):
        copy = self.library.copies[copy_id]
        member = self.library.members[member_id]

        copy.is_issued = False
        member.issued_books.remove(copy)
