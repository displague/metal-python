// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// CapacityLevelPerBaremetal capacity level per baremetal
//
// swagger:model CapacityLevelPerBaremetal
type CapacityLevelPerBaremetal struct {

	// level
	Level string `json:"level,omitempty"`
}

// Validate validates this capacity level per baremetal
func (m *CapacityLevelPerBaremetal) Validate(formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *CapacityLevelPerBaremetal) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *CapacityLevelPerBaremetal) UnmarshalBinary(b []byte) error {
	var res CapacityLevelPerBaremetal
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
