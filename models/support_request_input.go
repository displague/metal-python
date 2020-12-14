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

// SupportRequestInput support request input
//
// swagger:model SupportRequestInput
type SupportRequestInput struct {

	// device id
	DeviceID string `json:"device_id,omitempty"`

	// message
	// Required: true
	Message *string `json:"message"`

	// project id
	ProjectID string `json:"project_id,omitempty"`

	// subject
	// Required: true
	Subject *string `json:"subject"`

	// user id
	// Required: true
	UserID *string `json:"user_id"`
}

// Validate validates this support request input
func (m *SupportRequestInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateMessage(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateSubject(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateUserID(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *SupportRequestInput) validateMessage(formats strfmt.Registry) error {

	if err := validate.Required("message", "body", m.Message); err != nil {
		return err
	}

	return nil
}

func (m *SupportRequestInput) validateSubject(formats strfmt.Registry) error {

	if err := validate.Required("subject", "body", m.Subject); err != nil {
		return err
	}

	return nil
}

func (m *SupportRequestInput) validateUserID(formats strfmt.Registry) error {

	if err := validate.Required("user_id", "body", m.UserID); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *SupportRequestInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *SupportRequestInput) UnmarshalBinary(b []byte) error {
	var res SupportRequestInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
