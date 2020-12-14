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

// NewFindProjectBgpSessionsParams creates a new FindProjectBgpSessionsParams object
// with the default values initialized.
func NewFindProjectBgpSessionsParams() *FindProjectBgpSessionsParams {
	var ()
	return &FindProjectBgpSessionsParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindProjectBgpSessionsParamsWithTimeout creates a new FindProjectBgpSessionsParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindProjectBgpSessionsParamsWithTimeout(timeout time.Duration) *FindProjectBgpSessionsParams {
	var ()
	return &FindProjectBgpSessionsParams{

		timeout: timeout,
	}
}

// NewFindProjectBgpSessionsParamsWithContext creates a new FindProjectBgpSessionsParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindProjectBgpSessionsParamsWithContext(ctx context.Context) *FindProjectBgpSessionsParams {
	var ()
	return &FindProjectBgpSessionsParams{

		Context: ctx,
	}
}

// NewFindProjectBgpSessionsParamsWithHTTPClient creates a new FindProjectBgpSessionsParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindProjectBgpSessionsParamsWithHTTPClient(client *http.Client) *FindProjectBgpSessionsParams {
	var ()
	return &FindProjectBgpSessionsParams{
		HTTPClient: client,
	}
}

/*FindProjectBgpSessionsParams contains all the parameters to send to the API endpoint
for the find project bgp sessions operation typically these are written to a http.Request
*/
type FindProjectBgpSessionsParams struct {

	/*ID
	  Project UUID

	*/
	ID strfmt.UUID

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) WithTimeout(timeout time.Duration) *FindProjectBgpSessionsParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) WithContext(ctx context.Context) *FindProjectBgpSessionsParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) WithHTTPClient(client *http.Client) *FindProjectBgpSessionsParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) WithID(id strfmt.UUID) *FindProjectBgpSessionsParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find project bgp sessions params
func (o *FindProjectBgpSessionsParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *FindProjectBgpSessionsParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
