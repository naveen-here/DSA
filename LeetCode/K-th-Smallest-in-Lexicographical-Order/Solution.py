numOfChildren(curr, next, n) =
    (next - curr) +
    numOfChildren(curr * 10, next * 10, n)