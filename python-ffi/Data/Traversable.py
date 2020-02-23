def array1(a):
    return (a, )


def array2(a):
    return lambda b: (a, b)


def array3(a):
    return lambda b: lambda c: (a, b, c)


def concat2(xs):
    return lambda ys: (*xs, *ys)


def traverseArrayImpl(apply,
                      array1=array1,
                      array2=array2,
                      array3=array3,
                      concat2=concat2):
    def ap_map(map):
        def ap_pure(pure):
            def ap_f(f):
                def ap_array(array):
                    def go(bot, top):
                        gap = top - bot
                        return cases.get(gap, default)(bot, top, gap)

                    def default(
                        bot,
                        top,
                        gap,
                        # fast bind
                        concat2=concat2,
                        apply=apply,
                        go=go,
                        map=map):
                        pivot = bot + gap // 4 * 2
                        return apply(map(concat2)(go(bot,
                                                     pivot)))(go(pivot, top))

                    def case0(bot, top, gap, pure=pure):
                        return pure(())

                    def case1(bot,
                              top,
                              gap,
                              array1=array1,
                              f=f,
                              map=map,
                              array=array):
                        return map(array1)(f(array[bot]))

                    def case2(bot,
                              top,
                              gap,
                              apply=apply,
                              map=map,
                              f=f,
                              array2=array2,
                              array=array):
                        return apply(map(array2)(f(array[bot])))(f(array[bot +
                                                                         1]))

                    def case3(bot,
                              top,
                              gap,
                              apply=apply,
                              map=map,
                              array3=array3,
                              f=f,
                              array=array):
                        return apply(
                            apply(map(array3)(f(array[bot])))(f(
                                array[bot + 1])))(f(array[bot + 2]))

                    cases = {0: case0, 1: case1, 2: case2, 3: case3}

                    return go(0, len(array))

                return ap_array

            return ap_f

        return ap_pure

    return ap_map
