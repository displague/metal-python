// Code generated by go-swagger; DO NOT EDIT.

package projects

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// CreateLicenseReader is a Reader for the CreateLicense structure.
type CreateLicenseReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *CreateLicenseReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewCreateLicenseCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewCreateLicenseUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewCreateLicenseForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewCreateLicenseNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewCreateLicenseUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewCreateLicenseCreated creates a CreateLicenseCreated with default headers values
func NewCreateLicenseCreated() *CreateLicenseCreated {
	return &CreateLicenseCreated{}
}

/*CreateLicenseCreated handles this case with default header values.

created
*/
type CreateLicenseCreated struct {
	Payload *models.License
}

func (o *CreateLicenseCreated) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/licenses][%d] createLicenseCreated  %+v", 201, o.Payload)
}

func (o *CreateLicenseCreated) GetPayload() *models.License {
	return o.Payload
}

func (o *CreateLicenseCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.License)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCreateLicenseUnauthorized creates a CreateLicenseUnauthorized with default headers values
func NewCreateLicenseUnauthorized() *CreateLicenseUnauthorized {
	return &CreateLicenseUnauthorized{}
}

/*CreateLicenseUnauthorized handles this case with default header values.

unauthorized
*/
type CreateLicenseUnauthorized struct {
}

func (o *CreateLicenseUnauthorized) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/licenses][%d] createLicenseUnauthorized ", 401)
}

func (o *CreateLicenseUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateLicenseForbidden creates a CreateLicenseForbidden with default headers values
func NewCreateLicenseForbidden() *CreateLicenseForbidden {
	return &CreateLicenseForbidden{}
}

/*CreateLicenseForbidden handles this case with default header values.

forbidden
*/
type CreateLicenseForbidden struct {
}

func (o *CreateLicenseForbidden) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/licenses][%d] createLicenseForbidden ", 403)
}

func (o *CreateLicenseForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateLicenseNotFound creates a CreateLicenseNotFound with default headers values
func NewCreateLicenseNotFound() *CreateLicenseNotFound {
	return &CreateLicenseNotFound{}
}

/*CreateLicenseNotFound handles this case with default header values.

not found
*/
type CreateLicenseNotFound struct {
}

func (o *CreateLicenseNotFound) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/licenses][%d] createLicenseNotFound ", 404)
}

func (o *CreateLicenseNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateLicenseUnprocessableEntity creates a CreateLicenseUnprocessableEntity with default headers values
func NewCreateLicenseUnprocessableEntity() *CreateLicenseUnprocessableEntity {
	return &CreateLicenseUnprocessableEntity{}
}

/*CreateLicenseUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type CreateLicenseUnprocessableEntity struct {
}

func (o *CreateLicenseUnprocessableEntity) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/licenses][%d] createLicenseUnprocessableEntity ", 422)
}

func (o *CreateLicenseUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
