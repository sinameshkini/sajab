package service

import (
	"github.com/spf13/viper"
	"io"
	"log"
	"os"
	"sajab/pkg/config"
)

var(
	logger *log.Logger
	apiConfig *viper.Viper
)



func Run() (err error) {
	// init service config
	initConfig()
	// Init log file
	logger = initLogger(viper.GetString("log_file"))
	logger.Print("SAJAB Service Started (Dev: http://sottabyte.ir)")
	// init API config
	apiConfig, err = config.Init(logger)



	return
}

func initConfig()  {
	viper.SetConfigFile("config.json")
	err := viper.ReadInConfig()
	if err != nil {
		panic(err.Error())
	}
}

func initLogger(loggerFile string) *log.Logger {
	var (
		err     error
		logFile *os.File
	)

	// Open file in append mode
	logFile, err = os.OpenFile(loggerFile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		log.Fatalln(err)
	}

	// Create a multiWriter
	output := io.MultiWriter(os.Stderr, logFile)

	// Instantiation logger
	return log.New(output, "", log.Ldate|log.Ltime|log.Lmicroseconds)
}