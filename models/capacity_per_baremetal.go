// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// CapacityPerBaremetal capacity per baremetal
//
// swagger:model CapacityPerBaremetal
type CapacityPerBaremetal struct {

	// available servers
	AvailableServers int64 `json:"available_servers,omitempty"`

	// level
	Level string `json:"level,omitempty"`

	// market buffer percentage
	MarketBufferPercentage int64 `json:"market_buffer_percentage,omitempty"`

	// market floor price
	MarketFloorPrice float32 `json:"market_floor_price,omitempty"`

	// total servers
	TotalServers int64 `json:"total_servers,omitempty"`
}

// Validate validates this capacity per baremetal
func (m *CapacityPerBaremetal) Validate(formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *CapacityPerBaremetal) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *CapacityPerBaremetal) UnmarshalBinary(b []byte) error {
	var res CapacityPerBaremetal
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
