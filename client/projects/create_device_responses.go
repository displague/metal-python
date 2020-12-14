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

// CreateDeviceReader is a Reader for the CreateDevice structure.
type CreateDeviceReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *CreateDeviceReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewCreateDeviceCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewCreateDeviceUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewCreateDeviceForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewCreateDeviceNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewCreateDeviceUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewCreateDeviceCreated creates a CreateDeviceCreated with default headers values
func NewCreateDeviceCreated() *CreateDeviceCreated {
	return &CreateDeviceCreated{}
}

/*CreateDeviceCreated handles this case with default header values.

created
*/
type CreateDeviceCreated struct {
	Payload *models.Device
}

func (o *CreateDeviceCreated) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/devices][%d] createDeviceCreated  %+v", 201, o.Payload)
}

func (o *CreateDeviceCreated) GetPayload() *models.Device {
	return o.Payload
}

func (o *CreateDeviceCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.Device)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCreateDeviceUnauthorized creates a CreateDeviceUnauthorized with default headers values
func NewCreateDeviceUnauthorized() *CreateDeviceUnauthorized {
	return &CreateDeviceUnauthorized{}
}

/*CreateDeviceUnauthorized handles this case with default header values.

unauthorized
*/
type CreateDeviceUnauthorized struct {
}

func (o *CreateDeviceUnauthorized) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/devices][%d] createDeviceUnauthorized ", 401)
}

func (o *CreateDeviceUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateDeviceForbidden creates a CreateDeviceForbidden with default headers values
func NewCreateDeviceForbidden() *CreateDeviceForbidden {
	return &CreateDeviceForbidden{}
}

/*CreateDeviceForbidden handles this case with default header values.

forbidden
*/
type CreateDeviceForbidden struct {
}

func (o *CreateDeviceForbidden) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/devices][%d] createDeviceForbidden ", 403)
}

func (o *CreateDeviceForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateDeviceNotFound creates a CreateDeviceNotFound with default headers values
func NewCreateDeviceNotFound() *CreateDeviceNotFound {
	return &CreateDeviceNotFound{}
}

/*CreateDeviceNotFound handles this case with default header values.

not found
*/
type CreateDeviceNotFound struct {
}

func (o *CreateDeviceNotFound) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/devices][%d] createDeviceNotFound ", 404)
}

func (o *CreateDeviceNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateDeviceUnprocessableEntity creates a CreateDeviceUnprocessableEntity with default headers values
func NewCreateDeviceUnprocessableEntity() *CreateDeviceUnprocessableEntity {
	return &CreateDeviceUnprocessableEntity{}
}

/*CreateDeviceUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type CreateDeviceUnprocessableEntity struct {
}

func (o *CreateDeviceUnprocessableEntity) Error() string {
	return fmt.Sprintf("[POST /projects/{id}/devices][%d] createDeviceUnprocessableEntity ", 422)
}

func (o *CreateDeviceUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
