// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"strconv"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// DeviceUsageList device usage list
//
// swagger:model DeviceUsageList
type DeviceUsageList struct {

	// usages
	Usages []*DeviceUsage `json:"usages"`
}

// Validate validates this device usage list
func (m *DeviceUsageList) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateUsages(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *DeviceUsageList) validateUsages(formats strfmt.Registry) error {

	if swag.IsZero(m.Usages) { // not required
		return nil
	}

	for i := 0; i < len(m.Usages); i++ {
		if swag.IsZero(m.Usages[i]) { // not required
			continue
		}

		if m.Usages[i] != nil {
			if err := m.Usages[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("usages" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *DeviceUsageList) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *DeviceUsageList) UnmarshalBinary(b []byte) error {
	var res DeviceUsageList
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
