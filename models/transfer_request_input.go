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

// TransferRequestInput transfer request input
//
// swagger:model TransferRequestInput
type TransferRequestInput struct {

	// target organization id
	// Format: uuid
	TargetOrganizationID strfmt.UUID `json:"target_organization_id,omitempty"`
}

// Validate validates this transfer request input
func (m *TransferRequestInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateTargetOrganizationID(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *TransferRequestInput) validateTargetOrganizationID(formats strfmt.Registry) error {

	if swag.IsZero(m.TargetOrganizationID) { // not required
		return nil
	}

	if err := validate.FormatOf("target_organization_id", "body", "uuid", m.TargetOrganizationID.String(), formats); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *TransferRequestInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *TransferRequestInput) UnmarshalBinary(b []byte) error {
	var res TransferRequestInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
