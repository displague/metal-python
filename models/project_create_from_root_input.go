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

// ProjectCreateFromRootInput project create from root input
//
// swagger:model ProjectCreateFromRootInput
type ProjectCreateFromRootInput struct {

	// customdata
	Customdata string `json:"customdata,omitempty"`

	// name
	// Required: true
	Name *string `json:"name"`

	// organization id
	// Format: uuid
	OrganizationID strfmt.UUID `json:"organization_id,omitempty"`

	// payment method id
	// Format: uuid
	PaymentMethodID strfmt.UUID `json:"payment_method_id,omitempty"`
}

// Validate validates this project create from root input
func (m *ProjectCreateFromRootInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateName(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateOrganizationID(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validatePaymentMethodID(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *ProjectCreateFromRootInput) validateName(formats strfmt.Registry) error {

	if err := validate.Required("name", "body", m.Name); err != nil {
		return err
	}

	return nil
}

func (m *ProjectCreateFromRootInput) validateOrganizationID(formats strfmt.Registry) error {

	if swag.IsZero(m.OrganizationID) { // not required
		return nil
	}

	if err := validate.FormatOf("organization_id", "body", "uuid", m.OrganizationID.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *ProjectCreateFromRootInput) validatePaymentMethodID(formats strfmt.Registry) error {

	if swag.IsZero(m.PaymentMethodID) { // not required
		return nil
	}

	if err := validate.FormatOf("payment_method_id", "body", "uuid", m.PaymentMethodID.String(), formats); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *ProjectCreateFromRootInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *ProjectCreateFromRootInput) UnmarshalBinary(b []byte) error {
	var res ProjectCreateFromRootInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
