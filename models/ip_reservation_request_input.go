// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// IPReservationRequestInput IP reservation request input
//
// swagger:model IPReservationRequestInput
type IPReservationRequestInput struct {

	// comments
	Comments string `json:"comments,omitempty"`

	// customdata
	Customdata string `json:"customdata,omitempty"`

	// details
	Details string `json:"details,omitempty"`

	// facility
	Facility string `json:"facility,omitempty"`

	// fail on approval required
	FailOnApprovalRequired bool `json:"fail_on_approval_required,omitempty"`

	// quantity
	// Required: true
	Quantity *int64 `json:"quantity"`

	// tags
	Tags []string `json:"tags"`

	// type
	// Required: true
	Type *string `json:"type"`
}

// Validate validates this IP reservation request input
func (m *IPReservationRequestInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateQuantity(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateType(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *IPReservationRequestInput) validateQuantity(formats strfmt.Registry) error {

	if err := validate.Required("quantity", "body", m.Quantity); err != nil {
		return err
	}

	return nil
}

func (m *IPReservationRequestInput) validateType(formats strfmt.Registry) error {

	if err := validate.Required("type", "body", m.Type); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *IPReservationRequestInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *IPReservationRequestInput) UnmarshalBinary(b []byte) error {
	var res IPReservationRequestInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
