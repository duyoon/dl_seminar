program for_test
implicit none
    integer :: i, j
    do i=1, 100000
        do j=1, 10000
            if (i==100000 .and. j==10000) then
                write(*,*) 'FORTRAN: looping is over!!!'
            end if
        end do
    end do
end program for_test
