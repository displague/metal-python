// Code generated by go-swagger; DO NOT EDIT.

package projects

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
)

// NewFindIPReservationCustomdataParams creates a new FindIPReservationCustomdataParams object
// with the default values initialized.
func NewFindIPReservationCustomdataParams() *FindIPReservationCustomdataParams {
	var ()
	return &FindIPReservationCustomdataParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindIPReservationCustomdataParamsWithTimeout creates a new FindIPReservationCustomdataParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindIPReservationCustomdataParamsWithTimeout(timeout time.Duration) *FindIPReservationCustomdataParams {
	var ()
	return &FindIPReservationCustomdataParams{

		timeout: timeout,
	}
}

// NewFindIPReservationCustomdataParamsWithContext creates a new FindIPReservationCustomdataParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindIPReservationCustomdataParamsWithContext(ctx context.Context) *FindIPReservationCustomdataParams {
	var ()
	return &FindIPReservationCustomdataParams{

		Context: ctx,
	}
}

// NewFindIPReservationCustomdataParamsWithHTTPClient creates a new FindIPReservationCustomdataParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindIPReservationCustomdataParamsWithHTTPClient(client *http.Client) *FindIPReservationCustomdataParams {
	var ()
	return &FindIPReservationCustomdataParams{
		HTTPClient: client,
	}
}

/*FindIPReservationCustomdataParams contains all the parameters to send to the API endpoint
for the find IP reservation customdata operation typically these are written to a http.Request
*/
type FindIPReservationCustomdataParams struct {

	/*ID
	  Ip Reservation UUID

	*/
	ID strfmt.UUID
	/*ProjectID
	  Project UUID

	*/
	ProjectID strfmt.UUID

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) WithTimeout(timeout time.Duration) *FindIPReservationCustomdataParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) WithContext(ctx context.Context) *FindIPReservationCustomdataParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) WithHTTPClient(client *http.Client) *FindIPReservationCustomdataParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) WithID(id strfmt.UUID) *FindIPReservationCustomdataParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithProjectID adds the projectID to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) WithProjectID(projectID strfmt.UUID) *FindIPReservationCustomdataParams {
	o.SetProjectID(projectID)
	return o
}

// SetProjectID adds the projectId to the find IP reservation customdata params
func (o *FindIPReservationCustomdataParams) SetProjectID(projectID strfmt.UUID) {
	o.ProjectID = projectID
}

// WriteToRequest writes these params to a swagger request
func (o *FindIPReservationCustomdataParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	// path param project_id
	if err := r.SetPathParam("project_id", o.ProjectID.String()); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
