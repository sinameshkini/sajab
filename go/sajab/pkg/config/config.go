package config

import (
	"encoding/json"
	"errors"
	"fmt"
	"github.com/spf13/viper"
	"log"
	"net/http"
	"sajab/models"
)

var (
	logger *log.Logger
)

func Init(l *log.Logger) (config *viper.Viper, err error) {
	logger = l

	var (
		req  string
		resp *http.Response
		response models.ApiResponse
	)

	req = fmt.Sprintf("%s/server.php?action=station&imei=%s&station_index=%s",
		viper.GetString("base_url"),
		viper.GetString("imei"),
		viper.GetString("station_index"))

	logger.Printf("request: %s", req)

	resp, err = http.Get(req)
	defer resp.Body.Close()
	if err != nil {

	}

	if resp == nil{
		err = errors.New("API response is null")
		return
	}

	if err = json.NewDecoder(resp.Body).Decode(&response); err != nil{
		return
	}

	logger.Printf("response: %v", response)


	//fmt.Println(response)

	return
}
