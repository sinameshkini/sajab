package models

type ApiResponse struct {
	Message         string `json:"message"`
	Longitude       string `json:"longitude"`
	Latitude        string `json:"latitude"`
	Status          string `json:"status"`
	Name            string `json:"name"`
	Description     string `json:"description"`
	Price           string `json:"price"`
	HA              string `json:"ha"`
	HB              string `json:"hb"`
	Relay1          string `json:"relay_1"`
	Relay2          string `json:"relay_2"`
	Relay3          string `json:"relay_3"`
	Relay4          string `json:"relay_4"`
	Multi           string `json:"multi"`
	SamplingRate    string `json:"sampling_rate"`
	BiasValue       string `json:"bias_value"`
	Coefficent      string `json:"coefficent"`
	MaxLevel        string `json:"max_level"`
	HysteresisValue string `json:"hysteresis_value"`
	MobilePhone1    string `json:"mobile_phone_1"`
	MobilePhone2    string `json:"mobile_phone_2"`
	MobilePhone3    string `json:"mobile_phone_3"`
}
