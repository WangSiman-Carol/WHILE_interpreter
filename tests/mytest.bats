load harness

@test "mytest-1" {
  check 'x := true ? 1 : 2' '{x → 1}'
}

@test "mytest-2" {
  check 'x := false ? 1 : 2' '{x → 2}'
}

@test "mytest-3" {
  check 'x := -3 < -5 ? 1 : 2' '{x → 2}'
}

@test "mytest-4" {
  check 'x := -3 > -5 ? 2 * (-3) : 2 ** 3' '{x → -6}'
}

@test "mytest-5" {
    check 'a := [1,2,3,4,5]; x := a[3]' '{a → [1, 2, 3, 4, 5], x → 4}'
}
