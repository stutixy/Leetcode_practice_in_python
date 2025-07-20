type set map[string]struct{}

func createSet() set {
    return make(set)
}

func (s set) add(val string) {
    s[val] = struct{}{}
}

func (s set) exists(val string) bool {
    _,exists := s[val]
    return exists
}

func (s set) remove(val string) {
    delete(s, val)
}

func removeSubfolders(folder []string) []string {
    s := createSet()
    res := []string{}
    for _,v := range folder {
        s.add(v)
    }
    for _,v := range folder {
        for i:=len(v)-1; i>=0; i-- {
            if v[i] == '/' {
                if s.exists(v[0:i]){
                    s.remove(v)
                    break
                }
            }
        }
    }

    for v := range s {
        fmt.Println(v)
        res = append(res, v)
    }
    return res
}