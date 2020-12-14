// Code generated by go-swagger; DO NOT EDIT.

package plans

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

// NewFindPlansByProjectParams creates a new FindPlansByProjectParams object
// with the default values initialized.
func NewFindPlansByProjectParams() *FindPlansByProjectParams {
	var ()
	return &FindPlansByProjectParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindPlansByProjectParamsWithTimeout creates a new FindPlansByProjectParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindPlansByProjectParamsWithTimeout(timeout time.Duration) *FindPlansByProjectParams {
	var ()
	return &FindPlansByProjectParams{

		timeout: timeout,
	}
}

// NewFindPlansByProjectParamsWithContext creates a new FindPlansByProjectParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindPlansByProjectParamsWithContext(ctx context.Context) *FindPlansByProjectParams {
	var ()
	return &FindPlansByProjectParams{

		Context: ctx,
	}
}

// NewFindPlansByProjectParamsWithHTTPClient creates a new FindPlansByProjectParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindPlansByProjectParamsWithHTTPClient(client *http.Client) *FindPlansByProjectParams {
	var ()
	return &FindPlansByProjectParams{
		HTTPClient: client,
	}
}

/*FindPlansByProjectParams contains all the parameters to send to the API endpoint
for the find plans by project operation typically these are written to a http.Request
*/
type FindPlansByProjectParams struct {

	/*ID
	  Project UUID

	*/
	ID strfmt.UUID
	/*Include
	  related attributes to include

	*/
	Include *string

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find plans by project params
func (o *FindPlansByProjectParams) WithTimeout(timeout time.Duration) *FindPlansByProjectParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find plans by project params
func (o *FindPlansByProjectParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find plans by project params
func (o *FindPlansByProjectParams) WithContext(ctx context.Context) *FindPlansByProjectParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find plans by project params
func (o *FindPlansByProjectParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find plans by project params
func (o *FindPlansByProjectParams) WithHTTPClient(client *http.Client) *FindPlansByProjectParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find plans by project params
func (o *FindPlansByProjectParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the find plans by project params
func (o *FindPlansByProjectParams) WithID(id strfmt.UUID) *FindPlansByProjectParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find plans by project params
func (o *FindPlansByProjectParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithInclude adds the include to the find plans by project params
func (o *FindPlansByProjectParams) WithInclude(include *string) *FindPlansByProjectParams {
	o.SetInclude(include)
	return o
}

// SetInclude adds the include to the find plans by project params
func (o *FindPlansByProjectParams) SetInclude(include *string) {
	o.Include = include
}

// WriteToRequest writes these params to a swagger request
func (o *FindPlansByProjectParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Include != nil {

		// query param include
		var qrInclude string
		if o.Include != nil {
			qrInclude = *o.Include
		}
		qInclude := qrInclude
		if qInclude != "" {
			if err := r.SetQueryParam("include", qInclude); err != nil {
				return err
			}
		}

	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
