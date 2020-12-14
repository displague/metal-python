// Code generated by go-swagger; DO NOT EDIT.

package licenses

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// NewUpdateLicenseParams creates a new UpdateLicenseParams object
// with the default values initialized.
func NewUpdateLicenseParams() *UpdateLicenseParams {
	var ()
	return &UpdateLicenseParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewUpdateLicenseParamsWithTimeout creates a new UpdateLicenseParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewUpdateLicenseParamsWithTimeout(timeout time.Duration) *UpdateLicenseParams {
	var ()
	return &UpdateLicenseParams{

		timeout: timeout,
	}
}

// NewUpdateLicenseParamsWithContext creates a new UpdateLicenseParams object
// with the default values initialized, and the ability to set a context for a request
func NewUpdateLicenseParamsWithContext(ctx context.Context) *UpdateLicenseParams {
	var ()
	return &UpdateLicenseParams{

		Context: ctx,
	}
}

// NewUpdateLicenseParamsWithHTTPClient creates a new UpdateLicenseParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewUpdateLicenseParamsWithHTTPClient(client *http.Client) *UpdateLicenseParams {
	var ()
	return &UpdateLicenseParams{
		HTTPClient: client,
	}
}

/*UpdateLicenseParams contains all the parameters to send to the API endpoint
for the update license operation typically these are written to a http.Request
*/
type UpdateLicenseParams struct {

	/*ID
	  License UUID

	*/
	ID strfmt.UUID
	/*License
	  License to update

	*/
	License *models.LicenseUpdateInput

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the update license params
func (o *UpdateLicenseParams) WithTimeout(timeout time.Duration) *UpdateLicenseParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the update license params
func (o *UpdateLicenseParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the update license params
func (o *UpdateLicenseParams) WithContext(ctx context.Context) *UpdateLicenseParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the update license params
func (o *UpdateLicenseParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the update license params
func (o *UpdateLicenseParams) WithHTTPClient(client *http.Client) *UpdateLicenseParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the update license params
func (o *UpdateLicenseParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the update license params
func (o *UpdateLicenseParams) WithID(id strfmt.UUID) *UpdateLicenseParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the update license params
func (o *UpdateLicenseParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithLicense adds the license to the update license params
func (o *UpdateLicenseParams) WithLicense(license *models.LicenseUpdateInput) *UpdateLicenseParams {
	o.SetLicense(license)
	return o
}

// SetLicense adds the license to the update license params
func (o *UpdateLicenseParams) SetLicense(license *models.LicenseUpdateInput) {
	o.License = license
}

// WriteToRequest writes these params to a swagger request
func (o *UpdateLicenseParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.License != nil {
		if err := r.SetBodyParam(o.License); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
