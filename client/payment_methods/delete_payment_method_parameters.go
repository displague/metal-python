// Code generated by go-swagger; DO NOT EDIT.

package payment_methods

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

// NewDeletePaymentMethodParams creates a new DeletePaymentMethodParams object
// with the default values initialized.
func NewDeletePaymentMethodParams() *DeletePaymentMethodParams {
	var ()
	return &DeletePaymentMethodParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewDeletePaymentMethodParamsWithTimeout creates a new DeletePaymentMethodParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewDeletePaymentMethodParamsWithTimeout(timeout time.Duration) *DeletePaymentMethodParams {
	var ()
	return &DeletePaymentMethodParams{

		timeout: timeout,
	}
}

// NewDeletePaymentMethodParamsWithContext creates a new DeletePaymentMethodParams object
// with the default values initialized, and the ability to set a context for a request
func NewDeletePaymentMethodParamsWithContext(ctx context.Context) *DeletePaymentMethodParams {
	var ()
	return &DeletePaymentMethodParams{

		Context: ctx,
	}
}

// NewDeletePaymentMethodParamsWithHTTPClient creates a new DeletePaymentMethodParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewDeletePaymentMethodParamsWithHTTPClient(client *http.Client) *DeletePaymentMethodParams {
	var ()
	return &DeletePaymentMethodParams{
		HTTPClient: client,
	}
}

/*DeletePaymentMethodParams contains all the parameters to send to the API endpoint
for the delete payment method operation typically these are written to a http.Request
*/
type DeletePaymentMethodParams struct {

	/*ID
	  Payment Method UUID

	*/
	ID strfmt.UUID

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the delete payment method params
func (o *DeletePaymentMethodParams) WithTimeout(timeout time.Duration) *DeletePaymentMethodParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the delete payment method params
func (o *DeletePaymentMethodParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the delete payment method params
func (o *DeletePaymentMethodParams) WithContext(ctx context.Context) *DeletePaymentMethodParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the delete payment method params
func (o *DeletePaymentMethodParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the delete payment method params
func (o *DeletePaymentMethodParams) WithHTTPClient(client *http.Client) *DeletePaymentMethodParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the delete payment method params
func (o *DeletePaymentMethodParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the delete payment method params
func (o *DeletePaymentMethodParams) WithID(id strfmt.UUID) *DeletePaymentMethodParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the delete payment method params
func (o *DeletePaymentMethodParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *DeletePaymentMethodParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

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
