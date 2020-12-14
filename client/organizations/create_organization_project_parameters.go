// Code generated by go-swagger; DO NOT EDIT.

package organizations

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

// NewCreateOrganizationProjectParams creates a new CreateOrganizationProjectParams object
// with the default values initialized.
func NewCreateOrganizationProjectParams() *CreateOrganizationProjectParams {
	var ()
	return &CreateOrganizationProjectParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewCreateOrganizationProjectParamsWithTimeout creates a new CreateOrganizationProjectParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewCreateOrganizationProjectParamsWithTimeout(timeout time.Duration) *CreateOrganizationProjectParams {
	var ()
	return &CreateOrganizationProjectParams{

		timeout: timeout,
	}
}

// NewCreateOrganizationProjectParamsWithContext creates a new CreateOrganizationProjectParams object
// with the default values initialized, and the ability to set a context for a request
func NewCreateOrganizationProjectParamsWithContext(ctx context.Context) *CreateOrganizationProjectParams {
	var ()
	return &CreateOrganizationProjectParams{

		Context: ctx,
	}
}

// NewCreateOrganizationProjectParamsWithHTTPClient creates a new CreateOrganizationProjectParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewCreateOrganizationProjectParamsWithHTTPClient(client *http.Client) *CreateOrganizationProjectParams {
	var ()
	return &CreateOrganizationProjectParams{
		HTTPClient: client,
	}
}

/*CreateOrganizationProjectParams contains all the parameters to send to the API endpoint
for the create organization project operation typically these are written to a http.Request
*/
type CreateOrganizationProjectParams struct {

	/*ID
	  Organization UUID

	*/
	ID strfmt.UUID
	/*Project
	  Project to create

	*/
	Project *models.ProjectCreateInput

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the create organization project params
func (o *CreateOrganizationProjectParams) WithTimeout(timeout time.Duration) *CreateOrganizationProjectParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the create organization project params
func (o *CreateOrganizationProjectParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the create organization project params
func (o *CreateOrganizationProjectParams) WithContext(ctx context.Context) *CreateOrganizationProjectParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the create organization project params
func (o *CreateOrganizationProjectParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the create organization project params
func (o *CreateOrganizationProjectParams) WithHTTPClient(client *http.Client) *CreateOrganizationProjectParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the create organization project params
func (o *CreateOrganizationProjectParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the create organization project params
func (o *CreateOrganizationProjectParams) WithID(id strfmt.UUID) *CreateOrganizationProjectParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the create organization project params
func (o *CreateOrganizationProjectParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithProject adds the project to the create organization project params
func (o *CreateOrganizationProjectParams) WithProject(project *models.ProjectCreateInput) *CreateOrganizationProjectParams {
	o.SetProject(project)
	return o
}

// SetProject adds the project to the create organization project params
func (o *CreateOrganizationProjectParams) SetProject(project *models.ProjectCreateInput) {
	o.Project = project
}

// WriteToRequest writes these params to a swagger request
func (o *CreateOrganizationProjectParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Project != nil {
		if err := r.SetBodyParam(o.Project); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
