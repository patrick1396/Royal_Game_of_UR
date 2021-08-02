program game_of_ur
  implicit none

  type :: piece
     character(2) :: text
     integer :: position
  end type piece

  type :: square
     character(2)  :: text = "oo"
     integer       :: counter = -1
  end type square
  
  
  !Define kind for douple precision
  integer, parameter :: dp = selected_real_kind(15,300)
  type(square), dimension(0:7,0:2) :: board
  type(piece), dimension(0:13)  :: counters
  integer :: i, roll

  call Init_Board(board)

  call Init_Counters(counters)
  
  call Print_Board(board, counters)
  call Random_Seed()
  print *, Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()

contains

  subroutine Init_Board(board)
    implicit none
    type(square), dimension(0:7,0:2), intent(inout) :: board

    board(0,0)%text = "++"
    board(0,2)%text = "++"
    board(3,1)%text = "++"
    board(6,0)%text = "++"
    board(6,2)%text = "++"

    board(4,0)%text = "  "
    board(5,0)%text = "  "
    board(4,2)%text = "  "
    board(5,2)%text = "  "
    
  end subroutine Init_Board

  subroutine Init_Counters(counters)
    implicit none
    type(piece), dimension(0:13), intent(inout) :: counters

    integer                                      :: i, j, k
    character(1)                                 :: colour, number

    colour = "w"
    do i = 0,1
       k = i*7
       do j = 0,7
          write(number, '(I1)') j+1
          counters(j+k)%text = colour//number

          counters(j+k)%position = 0
       end do
       colour = "b"
    end do
    
    
  end subroutine Init_Counters

  subroutine Print_Board(board, counters)
    implicit none
    type(square), dimension(0:7,0:2), intent(in) :: board
    type(piece), dimension(0:13), intent(in) :: counters
    integer                                          :: i
    
    call system("clear")
    print *, ""
    print *, "    ",counters(0)%text," ",counters(1)%text," ",counters(2)%text," ",counters(3)%text," ",&
         &counters(4)%text," ",counters(5)%text," ",counters(6)%text
    print *, ""
    do i = 0,2
       print *, "  ", board(0,i)%text," ", board(1,i)%text," ", board(2,i)%text," ", board(3,i)%text," ",&
            &board(4,i)%text," ", board(5,i)%text," ", board(6,i)%text," ", board(7,i)%text
    end do

    print *, ""

    print *, "    ",counters(7)%text," ",counters(8)%text," ",counters(9)%text," ",counters(10)%text," ",&
         &counters(11)%text," ",counters(12)%text," ",counters(13)%text
    
  end subroutine print_board

  function Dice_Roll()
    implicit none
    integer :: Dice_Roll
    real(kind=dp) :: hold

    call Random_Number(hold)
    
    Dice_Roll = Nint(hold)
    
  end function Dice_Roll
  
end program game_of_ur
