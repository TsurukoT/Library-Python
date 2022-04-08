#-------------------------------------------------------------------------------
#	Name:	Tsuruko Terakawa
#	Project	6
#	Due	Date:	12/9/2016
#-------------------------------------------------------------------------------
#	Honor	Code	Statement:	I	received	no	assistance	on	this	assignment	that
#	violates	the	ethical	guidelines	set	forth	by	professor	and	class	syllabus.
#-------------------------------------------------------------------------------
#	References:	Piazza
#-------------------------------------------------------------------------------
#	Comments and	assumptions:
#-------------------------------------------------------------------------------
#	NOTE:	width	of	source	code	should	be	<=	80	characters	to	be	read	on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#							10								20								30								40								50								60								70								80
#-------------------------------------------------------------------------------

class Book:

	def __init__(self, author, title, book_id):
    # initializing all instances
		self.author = author
		self.title = title
		self.book_id = book_id

	def __str__(self):
	# return a string with string formatting method
		return ('Book("%s", "%s", %d)' %(self.author, self.title, self.book_id))

	def __repr__(self):
		return ('Book("%s", "%s", %d)' %(self.author, self.title, self.book_id))

	def __eq__(self, other):
	# check if the book itself is same with the other one 
		if (self.author == other.author) and (self.title == other.title) and (self.book_id == other.book_id):
			return True
		else:
			return False


class Patron:

	def __init__(self, name, patron_id, borroweds = None):
	# Initializing all instance variables
		self.name = name
		self.patron_id = patron_id
		if borroweds == None:
			self.borroweds = []
		else:
			self.borroweds = borroweds
	def __str__(self):
	# return a string with string formatting method
		return ('Patron("%s", %d, %s)' %(self.name, self.patron_id, str(self.borroweds)))
	
	def __repr__(self):
		return ('Patron("%s", %d, %s)' %(self.name, self.patron_id, str(self.borroweds)))
	
	def return_book(self, library, book_id):
	# This function uses the reshelve_book method in the class Library
	    try:
	    # first try using the reshelve_book method from the libray by calling the function
	        mylib = Library(self)
	        library.reshelve_book(self.patron_id, book_id)
	        return True
	    # Then if returned any error, put it in exception and return False
	    except Exception:
	        return False

	def check_out_book_by_id(self, library, book_id):
		# This was really similar to return_book above, but used the loan_book method form the class library
	    try:
	    # check if loan_book works, and if return any exception from loan_books, return false
	        mylib = Library(self)
	        library.loan_book(self.patron_id, book_id)
	        return True
	    except:
	        return False
	def check_out_book_by_title(self, library, title):
		# it is similar to the two functions above, but this one since the title was given as the instance variable, the search by title from the class 
		#library was used to return a book instance first
	    try:
	        mylib = library
	        thebook = mylib.book_by_title(title)
	        mylib.loan_book(self.patron_id, thebook.book_id)
	        return True
	    except Exception:
	        return False


class DuplicateIdError (Exception):
	# Constructed DuplicateError here 

	def __init__(self, id, category = "Book"):
		self.id = id
		self.category = category
		# if category was given, use the given category
	def __str__(self):
		return ('duplicate %s ID: #%d' %(self.category, self.id))
	def __repr__(self):
		return ('duplicate %s ID: #%d' %(self.category, self.id))


class MissingIdError (LookupError):
	# Constructed a MissingIdError Exception here

	def __init__(self, id, category = "Book"):
		self.id = id
		self.category = category
	def __str__(self):
		return ('%s #%d not found' %(self.category, self.id))
	def __repr__(self):
		return ('%s #%d not found' %(self.category, self.id))


class Library:
	# Construct all instance variables here
	def __init__(self, books = None, patrons = None):
		# if book or patrons was none, they are empty list. If not they are what the user given
		if books == None:
			self.books = []
		else:
			self.books = books
		if patrons == None:
			self.patrons = []
		else:
			self.patrons = patrons
	def __str__(self):
		return("Library(%s, %s)" %(self.books, self.patrons))
	def __repr__(self):
		return("Library(%s, %s)" %(self.books, self.patrons))
	def admit_patron(self, patron):
		# if patron was in library already, raise duplicate error
		if patron in self.patrons:
			raise DuplicateIdError(patron.patron_id, "Patron")
			# if not, append the patron to library
		else:
			self.patrons.append(patron)

	def patron_by_id(self, patron_id):
		# search the patron by the id
		for pats in self.patrons:
			if pats.patron_id == patron_id:
			# if there is a patron which his id is same with the patron_id given return the patron
				return pats
		else:
			# if not, raise missin error
			raise MissingIdError(patron_id, "Patron")

	def book_by_id(self, book_id):
		# if there is a book in library which its id is the same with the given book_id, return the info of the book
		for book in self.books:
			if book.book_id == book_id:
				return book
		else: 
			# else, raise the missin error
			raise MissingIdError(book_id, "Book")

	def book_by_title(self, title):
		# search for the book through library with the book title
	    for book in self.books:
	    	# for all book in the library, if there is one book that the title is same with the given title, return the info of that book
	        if book.title == title:
	            return book
	        # else, raise look up error, if could not find the book with same title
	    else:
		    raise LookupError('no book found with the title "%s"' %(title))
		    # also raise look up error when the library book list was empty
	    if self.books == []:
		    raise LookupError('no book found with the title "%s"' %(title))
		

	def donate_book(self, book):
		# onlyforid was buit as a empty list to store book ids of the books in the library
	    onlyforid = []
	    for allbook in self.books:
	        onlyforid.append(allbook.book_id)
	        # check if the given book's book_id is in the onlyforid, if not append it to the book list of library
	    if book.book_id not in onlyforid:
	        self.books.append(book)
	        # if there is already a same id in only for id, raise duplicate id error
	    else:
	        raise DuplicateIdError(book.book_id, "Book")

	def loan_book(self, patron_id, book_id):
		# The four empty list was built each for storing the borrowed books ids,
	    onlyforbbid = []
	    # book ids of books in library, 
	    onlyforlbid = []
	    # patron ids of patrons in library,
	    onlyforpid = []
	    # and the patrons in library
	    onlyforpat = []
	    # this way I can check if the book or patron is in a specific place by see if their id is there or not
	    for patron in self.patrons:
	    	# storing variables for patron_id
	        onlyforpid.append(patron.patron_id)
	        for borrowed in patron.borroweds:
	        	# storing variables for borrowed books' id
	            onlyforbbid.append(borrowed.book_id)
	    for allbook in self.books:
	    	# storing variables for ids for books in library
	        onlyforlbid.append(allbook.book_id)
	    if patron_id not in onlyforpid:
	    	# if patron not in library, missingiderror
	        raise MissingIdError(patron_id, "Patron")
	    if book_id not in onlyforlbid:
	    	# if book not in library, missingiderror
	        raise MissingIdError(book_id, "Book")
	    if book_id in onlyforbbid:
	    	# if the patron borrowing the book alredy have the book, duplicateerror
	        raise DuplicateIdError(book_id, "Book")
	    else:
	    	# anything else, no error, but append the book to the borrowing patron and remove the book from library
	        for patron in self.patrons:
	            if patron.patron_id == patron_id:
	               onlyforpat.append(patron)
	               for book in self.books:
	                   if book.book_id == book_id:
	                       self.books.remove(book)
	                       patron.borroweds.append(book)


	def reshelve_book(self, patron_id, book_id):
		# The three empty list was built each for storing the borrowed books ids,
	    onlyforbbid = []
	    # the book_id for books in library
	    onlyforlbid = []
	    # and the patron_ id for patrons in library
	    onlyforpid = []
	    for patron in self.patrons:
	    	# storing variables for patron_id
	        onlyforpid.append(patron.patron_id)
	        for borrowed in patron.borroweds:
	        	# storing variables for borrowed books' id
	            onlyforbbid.append(borrowed.book_id)
	    for allbook in self.books:
	    	# storing variables for ids for books in library
	        onlyforlbid.append(allbook.book_id)
	    if book_id in onlyforlbid:
	    	# if the book is already in library, raise duplicateerror
	        raise DuplicateIdError(book_id, "Book")
	    if patron_id not in onlyforpid:
	    	# if the patron does not belong to this library, raise missing id error
	        raise MissingIdError(patron_id, "Patron")
	    if book_id not in onlyforbbid:
	    	# if the book is not in the patron's book list, alre raise missing id error
	        raise MissingIdError(book_id, "Book")
	    else:
	    	# anything else, no error. Append the returning book to library book list, remove the returning book from the patron's book list
	        for patron in self.patrons:
	            if patron.patron_id == patron_id:
	                for borrowed in patron.borroweds:
	                    if borrowed.book_id == book_id:
	                        self.books.append(borrowed)
	                        patron.borroweds.remove(borrowed)

