class Hall:

    def __init__(self,row,col,hall_no):
        self.__seats={}
        self.__show_list=[]
        self.__row=row
        self.__col=col
        self.__hall_no=hall_no

    def entry_show(self,id,movie_name,time):
        info=(id,movie_name,time)
        self.show_list.append(info)
        seat=[[0 for _ in range(self.__col)]for _ in range(self.__row)]
        self.__seats[id] = seat

    def Book_seats(self,id,row,col):
        if id not in self.__seats:
            
            print(f'Show id: {id} does not Exist !')
            return

        if col< 0 or row < 0 or row >= self.__row or col >=self.__col:
            print(f'Invalid Area !') 
            return

        elif self.__seats[id][row][col] == 1:
            
            print(f'This seat ({row},{col}) is already Booked ')
            return
        
        else:
            self.__seats[id][row][col]=1
            print(f'seats ({row} , {col}) booked for show {id}')

    
    def view_show_list(self):
        print('----------------------------------------------------------')
        for sh in self.__show_list:
            print(f'MOVIENAME: {sh[1]}  SHOW ID: {sh[0]}  TIME: {sh[2]}')
        print('----------------------------------------------------------')

    def view_available_seats(self,id):
        if id not in self.__seats:
            print(f'Show id: {id} does not Exist !')
            return
        seat = self.__seats[id]

        print('True for available seat otherwise  seat is Booked already')
        print('\n')
        print(f'Available seats for show {id}:')
        for i in range(self.__row):
            for j in range(self.__col):
                if self.seats[id][i][j]==0:
                    print(f'Seat {i,j}')
                
        print('\n')
        print(f'Update Seats Matrix for {self.__hall_no}:')
        print('\n')
        for row in seat:
            print(row)
        print('\n')

    @property
    def hall_no(self):
        return self.__hall_no
    @property
    def show_list(self):
        return self.__show_list
    @property
    def row(self):
        return self.__row
    @property
    def col(self):
        return self.__col
    @property
    def seats(self):
        return self.__seats

class Star_Cinema(Hall):

    hall_list = []

    @classmethod
    def entry_hall(self,hl):
        self.hall_list.append(hl)



hall = Hall(5,5,'Hall 1')
hall.entry_show('111','Jawan Maji(111)','20/7/2024 11:00 AM')
hall.entry_show('333','Sujon Maji(333)','11/7/2024 4:00 PM')

Star_Cinema.entry_hall(hall)

while True:
    print('1. VIEW ALL SHOW TODAY ')
    print('2. VIEW AVAILABLE SEATS ')
    print('3. BOOK TICKET ')
    print('4. Exit ')

    op =int(input('ENTER OPTION: '))

    if op == 1:
        hall.view_show_list()
    elif op == 2:
        id = str(input('ENTER SHOW ID: '))
        hall.view_available_seats(id)
    elif op == 3:
        id = str(input('Show Id: '))
        ticket =int( input('Number of Ticket? : '))
        row = int(input('Enter Seat Row: '))
        col = int(input('Enter Seat Col: '))
        hall.Book_seats(id,row,col)

    elif op == 4:
        break
