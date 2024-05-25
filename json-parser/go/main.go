package main

import (
	"bytes"
	"os"
	"strings"
)

func jsonparser(data []byte) {
	mine := bytes.NewBuffer(data).String()
	for i := 0; i < len(string(mine)); i++ {
		//println(strings.Split(string(data), "\"")[i], len(data))
		println(string(mine)[i], len(mine))
	}
	println(strings.Split(string(data), "\"")[0], len(data))
	// for _, s := range string(data) {
	// 	//"{ \"name\": \"test\", \"version\": \"1.0.0\", \"dependencies\": {"
	// 	fmt.Println(s)
	// for i := 0; i < len(s); i++ {
	// 	if s[i] == '{' {
	// 		fmt.Println(s[:i])
	// 		break
	// 	}
	// }
	//fmt.Println(strings.Split(s[:], "\"")[1])
	//}
}

func main() {
	plan, _ := os.ReadFile("test.json")
	jsonparser(plan)

}
