program game_of_ur
  implicit none

  type :: piece
     character(2), dimension(0:1) :: text
     integer :: position
  end type piece

  type :: square
     character(2)  :: text = "oo"
     integer       :: counter = -1
  end type square
  
  
  !Define kind for douple precision
  integer, parameter :: dp = selected_real_kind(15,300)
  type(square), dimension(0:7,0:2)   :: board
  type(square), dimension(0:15,0:1)  :: off_board
  type(piece), dimension(0:13)       :: counters
  integer :: i
  integer, dimension(0:1, 1:14, 0:2) :: pos_map
  integer                            :: turn = 0
  integer                            :: roll

  call Init_Board(board, off_board)

  call Init_Counters(counters)

  call Init_Pos_Map(pos_map)

  
  call Random_Seed()
  roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll() 
  call Print_Board(board, off_board, counters, roll)

contains

  subroutine Init_Board(board, off_board)
    implicit none
    type(square), dimension(0:7,0:2), intent(inout)  :: board
    type(square), dimension(0:15,0:1), intent(inout) :: off_board

    integer                                          :: i, j
    
    board(0,0)%text = "++"
    board(0,2)%text = "++"
    board(3,1)%text = "++"
    board(6,0)%text = "++"
    board(6,2)%text = "++"

    board(4,0)%text = "  "
    board(5,0)%text = "  "
    board(4,2)%text = "  "
    board(5,2)%text = "  "

    do i = 0,1
       do j = 0, 15
          off_board(j, i)%text = "__"
       end do
       off_board(0,i)%text = "S:"
       off_board(7,i)%text = "F:"
    end do
    
  end subroutine Init_Board

  subroutine Init_Counters(counters)
    implicit none
    type(piece), dimension(0:13), intent(inout) :: counters

    integer                                     :: i, j, k, l
    character(1)                                :: upp_colour, colour, number

    colour = "w"
    upp_colour = "W"
    do i = 0,1
       k = i*7
       do j = 0,6
          l = j+k
          write(number, '(I1)') j+1
          counters(l)%text(0) = colour//number
          counters(l)%text(1) = upp_colour//number
          counters(l)%position = 0
       end do
       colour = "b"
       upp_colour = "B"
    end do
  end subroutine Init_Counters

  subroutine Init_Pos_Map(pos_map)
    implicit none
    integer, dimension(0:1, 1:14, 0:1), intent(inout) :: pos_map

    !Mapping of white positions
    pos_map(0,1,0) = 3
    pos_map(0,1,1) = 2

    pos_map(0,2,0) = 2
    pos_map(0,2,1) = 2

    pos_map(0,3,0) = 1
    pos_map(0,3,1) = 2

    pos_map(0,4,0) = 0
    pos_map(0,4,1) = 2

    pos_map(0,5,0) = 0
    pos_map(0,5,1) = 1

    pos_map(0,6,0) = 1
    pos_map(0,6,1) = 1

    pos_map(0,7,0) = 2
    pos_map(0,7,1) = 1

    pos_map(0,8,0) = 3
    pos_map(0,8,1) = 1

    pos_map(0,9,0) = 4
    pos_map(0,9,1) = 1

    pos_map(0,10,0) = 5
    pos_map(0,10,1) = 1

    pos_map(0,11,0) = 6
    pos_map(0,11,1) = 1

    pos_map(0,12,0) = 7
    pos_map(0,12,1) = 1

    pos_map(0,13,0) = 7
    pos_map(0,13,1) = 2

    pos_map(0,14,0) = 6
    pos_map(0,14,1) = 2


    !Mapping of black positions
    pos_map(0,1,0) = 3
    pos_map(0,1,1) = 0

    pos_map(0,2,0) = 2
    pos_map(0,2,1) = 0

    pos_map(0,3,0) = 1
    pos_map(0,3,1) = 0

    pos_map(0,4,0) = 0
    pos_map(0,4,1) = 0

    pos_map(0,5,0) = 0
    pos_map(0,5,1) = 1

    pos_map(0,6,0) = 1
    pos_map(0,6,1) = 1

    pos_map(0,7,0) = 2
    pos_map(0,7,1) = 1

    pos_map(0,8,0) = 3
    pos_map(0,8,1) = 1

    pos_map(0,9,0) = 4
    pos_map(0,9,1) = 1

    pos_map(0,10,0) = 5
    pos_map(0,10,1) = 1

    pos_map(0,11,0) = 6
    pos_map(0,11,1) = 1

    pos_map(0,12,0) = 7
    pos_map(0,12,1) = 1

    pos_map(0,13,0) = 7
    pos_map(0,13,1) = 0

    pos_map(0,14,0) = 6
    pos_map(0,14,1) = 0

  end subroutine Init_Pos_Map
  
  subroutine Print_Board(board, off_board, counters, roll)
    implicit none
    type(square), dimension(0:7,0:2), intent(in)  :: board
    type(square), dimension(0:15,0:1), intent(in) :: off_board
    type(piece), dimension(0:13), intent(in)      :: counters
    integer, intent(in)                           :: roll
    integer                                       :: i, j, index
    
    call system("clear")

    write(*,*) roll
    do i = 0, 15
       index = off_board(i,0)%counter
       if (index.eq.-1) then
          write(*, '(A2)', advance = 'No') off_board(i, 0)%text
       else
          write(*, '(A2)', advance = 'No') counters(index)%text(0)
       end if
       write(*, '(A2)', advance = 'No') " "
    end do
    write(*,*)
    write(*,*)
   
    do i = 0,2
       do j = 0,7
          write(*, '(A2)', advance = 'No') board(j, i)%text
          write(*, '(A2)', advance = 'No') " "
       end do
       write(*,*)
    end do
    
    write(*,*)

    do i = 0, 15
       index = off_board(i,0)%counter
       if (index.eq.-1) then
          write(*, '(A2)', advance = 'No') off_board(i, 0)%text
       else
          write(*, '(A2)', advance = 'No') counters(index)%text(0)
       end if
       write(*, '(A2)', advance = 'No') " "
    end do
    write(*,*)
    
  end subroutine print_board

  function Dice_Roll()
    implicit none
    integer :: Dice_Roll
    real(kind=dp) :: hold

    call Random_Number(hold)
    
    Dice_Roll = Nint(hold)
    
  end function Dice_Roll
  
end program game_of_ur
