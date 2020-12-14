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

// PaymentMethodCreateInput payment method create input
//
// swagger:model PaymentMethodCreateInput
type PaymentMethodCreateInput struct {

	// default
	Default bool `json:"default,omitempty"`

	// name
	// Required: true
	Name *string `json:"name"`

	// nonce
	// Required: true
	Nonce *string `json:"nonce"`
}

// Validate validates this payment method create input
func (m *PaymentMethodCreateInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateName(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateNonce(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *PaymentMethodCreateInput) validateName(formats strfmt.Registry) error {

	if err := validate.Required("name", "body", m.Name); err != nil {
		return err
	}

	return nil
}

func (m *PaymentMethodCreateInput) validateNonce(formats strfmt.Registry) error {

	if err := validate.Required("nonce", "body", m.Nonce); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *PaymentMethodCreateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *PaymentMethodCreateInput) UnmarshalBinary(b []byte) error {
	var res PaymentMethodCreateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
