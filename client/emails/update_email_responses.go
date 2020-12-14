// Code generated by go-swagger; DO NOT EDIT.

package emails

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// UpdateEmailReader is a Reader for the UpdateEmail structure.
type UpdateEmailReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *UpdateEmailReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewUpdateEmailOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewUpdateEmailUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewUpdateEmailForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewUpdateEmailNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewUpdateEmailUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewUpdateEmailOK creates a UpdateEmailOK with default headers values
func NewUpdateEmailOK() *UpdateEmailOK {
	return &UpdateEmailOK{}
}

/*UpdateEmailOK handles this case with default header values.

ok
*/
type UpdateEmailOK struct {
	Payload *models.Email
}

func (o *UpdateEmailOK) Error() string {
	return fmt.Sprintf("[PUT /emails/{id}][%d] updateEmailOK  %+v", 200, o.Payload)
}

func (o *UpdateEmailOK) GetPayload() *models.Email {
	return o.Payload
}

func (o *UpdateEmailOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.Email)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewUpdateEmailUnauthorized creates a UpdateEmailUnauthorized with default headers values
func NewUpdateEmailUnauthorized() *UpdateEmailUnauthorized {
	return &UpdateEmailUnauthorized{}
}

/*UpdateEmailUnauthorized handles this case with default header values.

unauthorized
*/
type UpdateEmailUnauthorized struct {
}

func (o *UpdateEmailUnauthorized) Error() string {
	return fmt.Sprintf("[PUT /emails/{id}][%d] updateEmailUnauthorized ", 401)
}

func (o *UpdateEmailUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateEmailForbidden creates a UpdateEmailForbidden with default headers values
func NewUpdateEmailForbidden() *UpdateEmailForbidden {
	return &UpdateEmailForbidden{}
}

/*UpdateEmailForbidden handles this case with default header values.

forbidden
*/
type UpdateEmailForbidden struct {
}

func (o *UpdateEmailForbidden) Error() string {
	return fmt.Sprintf("[PUT /emails/{id}][%d] updateEmailForbidden ", 403)
}

func (o *UpdateEmailForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateEmailNotFound creates a UpdateEmailNotFound with default headers values
func NewUpdateEmailNotFound() *UpdateEmailNotFound {
	return &UpdateEmailNotFound{}
}

/*UpdateEmailNotFound handles this case with default header values.

not found
*/
type UpdateEmailNotFound struct {
}

func (o *UpdateEmailNotFound) Error() string {
	return fmt.Sprintf("[PUT /emails/{id}][%d] updateEmailNotFound ", 404)
}

func (o *UpdateEmailNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewUpdateEmailUnprocessableEntity creates a UpdateEmailUnprocessableEntity with default headers values
func NewUpdateEmailUnprocessableEntity() *UpdateEmailUnprocessableEntity {
	return &UpdateEmailUnprocessableEntity{}
}

/*UpdateEmailUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type UpdateEmailUnprocessableEntity struct {
}

func (o *UpdateEmailUnprocessableEntity) Error() string {
	return fmt.Sprintf("[PUT /emails/{id}][%d] updateEmailUnprocessableEntity ", 422)
}

func (o *UpdateEmailUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
