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
  integer, dimension(0:6)            :: move_mask
  integer                            :: roll
  integer                            :: round, turn
 
  !setup
  call Init_Board(board, off_board)

  call Init_Counters(counters)

  call Init_Pos_Map(pos_map)
  
  call Random_Seed()
  

  round = -1
  call system("clear")

  if (round.lt.0) then
     round = Who_Goes_First()
  end if
  turn = modulo(round,2)

  call Counter_Positions(board, off_board, counters, pos_map)

  roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
  move_mask(:) = 0
  move_mask = Find_Valid_Moves(counters, board, pos_map, turn, roll)
  call Print_Board(board, off_board, counters, roll, turn)

contains

  function Find_Valid_Moves(counters, board, pos_map, turn, roll) result(move_mask)
    implicit none
    type(piece), dimension(0:13), intent(in)         :: counters
    type(square), dimension(0:7,0:2), intent(inout)  :: board
    integer, dimension(0:1, 1:14, 0:1), intent(in)   :: pos_map
    integer, intent(in)                              :: roll
    integer, intent(in)                              :: turn

    integer, dimension(0:6)                          :: move_mask
    integer                                          :: i
    integer                                          :: check_pos, target_counter
    integer                                          :: ind_1, ind_2


    print *, turn
    do i = 0+7*turn, 6+7*turn
       check_pos = counters(i)%position + roll
       if (check_pos.gt.15) then
          move_mask(i-7*turn) = 0
          cycle
       end if
       
       ind_1 = pos_map(0, check_pos, turn)
       ind_2 = pos_map(1, check_pos, turn)

       target_counter = board(ind_1, ind_2)%counter 

       if (target_counter .eq. -1) then
          move_mask(i-7*turn) = 1
       elseif ((ind_1.eq.3).and.(ind_2.eq.1).and.(target_counter.ne.-1)) then
          move_mask(i-7*turn) = 0

       elseif (modulo(target_counter, 7).eq.turn) then
          move_mask(i-7*turn) = 0
       else
          move_mask(i-7*turn) = 1
       end if
       
    end do

    
    
  end function Find_Valid_Moves
  
  function Who_Goes_First() result(player)
    implicit none

    integer :: player
    
    integer :: w_roll, b_roll
    logical :: found

    found = .false.


    do while (found.eqv..false.)
       w_roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
       print *, "White rolled: ", w_roll
       print *, ""
       b_roll = Dice_Roll()+Dice_Roll()+Dice_Roll()+Dice_Roll()
       print *, "Black rolled: ", b_roll
       print *, ""

       if (w_roll.gt.b_roll) then
          print *, "White goes first"
          player = 0
          found = .true.
       elseif (b_roll.gt.w_roll) then
          print *, "Black goes first"
          player = 1
          found = .true.
       else
          print *, "Draw, reroll"
          found = .false.
       end if
       
    end do

  end function Who_Goes_First

  subroutine Counter_Positions(board, off_board, counters, pos_map)
    implicit none
    type(square), dimension(0:7,0:2), intent(inout)  :: board
    type(square), dimension(0:15,0:1), intent(inout) :: off_board
    type(piece), dimension(0:13), intent(in)         :: counters
    integer, dimension(0:1, 1:14, 0:1), intent(in)   :: pos_map
    
    integer                                       :: i
    integer                                       :: ind_1, ind_2
    
    do i = 0,13
       if (counters(i)%position.eq.0) then
          off_board(modulo(i,7)+1,floor(i/7.0_dp))%counter = i
       elseif (counters(i)%position.eq.15) then
          off_board(modulo(i,7)+9,floor(i/7.0_dp))%counter = i
!       else
          !         ind_1 = pos_map(floor(i/7.0_dp)
       end if
    end do
    
  end subroutine Counter_Positions

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
       off_board(8,i)%text = "F:"
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
    pos_map(1,1,0) = 2

    pos_map(0,2,0) = 2
    pos_map(1,2,0) = 2

    pos_map(0,3,0) = 1
    pos_map(1,3,0) = 2

    pos_map(0,4,0) = 0
    pos_map(1,4,0) = 2

    pos_map(0,5,0) = 0
    pos_map(1,5,0) = 1

    pos_map(0,6,0) = 1
    pos_map(1,6,0) = 1

    pos_map(0,7,0) = 2
    pos_map(1,7,0) = 1

    pos_map(0,8,0) = 3
    pos_map(1,8,0) = 1

    pos_map(0,9,0) = 4
    pos_map(1,9,0) = 1

    pos_map(0,10,0) = 5
    pos_map(1,10,0) = 1

    pos_map(0,11,0) = 6
    pos_map(1,11,0) = 1

    pos_map(0,12,0) = 7
    pos_map(1,12,0) = 1

    pos_map(0,13,0) = 7
    pos_map(1,13,0) = 2

    pos_map(0,14,0) = 6
    pos_map(1,14,0) = 2


    !Mapping of black positions
    pos_map(0,1,1) = 3
    pos_map(1,1,1) = 0

    pos_map(0,2,1) = 2
    pos_map(1,2,1) = 0

    pos_map(0,3,1) = 1
    pos_map(1,3,1) = 0

    pos_map(0,4,1) = 0
    pos_map(1,4,1) = 0

    pos_map(0,5,1) = 0
    pos_map(1,5,1) = 1

    pos_map(0,6,1) = 1
    pos_map(1,6,1) = 1

    pos_map(0,7,1) = 2
    pos_map(1,7,1) = 1

    pos_map(0,8,1) = 3
    pos_map(1,8,1) = 1

    pos_map(0,9,1) = 4
    pos_map(1,9,1) = 1

    pos_map(0,10,1) = 5
    pos_map(1,10,1) = 1

    pos_map(0,11,1) = 6
    pos_map(1,11,1) = 1

    pos_map(0,12,1) = 7
    pos_map(1,12,1) = 1

    pos_map(0,13,1) = 7
    pos_map(1,13,1) = 0

    pos_map(0,14,1) = 6
    pos_map(1,14,1) = 0

  end subroutine Init_Pos_Map
  
  subroutine Print_Board(board, off_board, counters, roll, turn)
    implicit none
    type(square), dimension(0:7,0:2), intent(in)  :: board
    type(square), dimension(0:15,0:1), intent(in) :: off_board
    type(piece), dimension(0:13), intent(in)      :: counters
   ! integer, dimension(0:6), intent(in)           :: move_mask
    integer, intent(in)                           :: roll
    integer, intent(in)                           :: turn
    integer                                       :: i, j, index

    
    
    write(*,*) ""
    if (turn.eq.0) then
       write(*,*) "White rolled: ", roll
    else
       write(*,*) "Black rolled: ", roll
    end if
    do i = 0, 15
       index = off_board(i,1)%counter
       if (index.eq.-1) then
          write(*, '(A2)', advance = 'No') off_board(i, 0)%text
        elseif (turn.eq.1) then
           write(*, '(A2)', advance = 'No') counters(index)%text(0+move_mask(index-7))
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
       elseif (turn.eq.0) then
          write(*, '(A2)', advance = 'No') counters(index)%text(0+move_mask(index))
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
