// Code generated by go-swagger; DO NOT EDIT.

package invitations

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/models"
)

// CreateOrganizationInvitationReader is a Reader for the CreateOrganizationInvitation structure.
type CreateOrganizationInvitationReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *CreateOrganizationInvitationReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 201:
		result := NewCreateOrganizationInvitationCreated()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewCreateOrganizationInvitationUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 403:
		result := NewCreateOrganizationInvitationForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewCreateOrganizationInvitationNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewCreateOrganizationInvitationUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewCreateOrganizationInvitationCreated creates a CreateOrganizationInvitationCreated with default headers values
func NewCreateOrganizationInvitationCreated() *CreateOrganizationInvitationCreated {
	return &CreateOrganizationInvitationCreated{}
}

/*CreateOrganizationInvitationCreated handles this case with default header values.

created
*/
type CreateOrganizationInvitationCreated struct {
	Payload *models.Invitation
}

func (o *CreateOrganizationInvitationCreated) Error() string {
	return fmt.Sprintf("[POST /organizations/{id}/invitations][%d] createOrganizationInvitationCreated  %+v", 201, o.Payload)
}

func (o *CreateOrganizationInvitationCreated) GetPayload() *models.Invitation {
	return o.Payload
}

func (o *CreateOrganizationInvitationCreated) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.Invitation)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCreateOrganizationInvitationUnauthorized creates a CreateOrganizationInvitationUnauthorized with default headers values
func NewCreateOrganizationInvitationUnauthorized() *CreateOrganizationInvitationUnauthorized {
	return &CreateOrganizationInvitationUnauthorized{}
}

/*CreateOrganizationInvitationUnauthorized handles this case with default header values.

unauthorized
*/
type CreateOrganizationInvitationUnauthorized struct {
}

func (o *CreateOrganizationInvitationUnauthorized) Error() string {
	return fmt.Sprintf("[POST /organizations/{id}/invitations][%d] createOrganizationInvitationUnauthorized ", 401)
}

func (o *CreateOrganizationInvitationUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateOrganizationInvitationForbidden creates a CreateOrganizationInvitationForbidden with default headers values
func NewCreateOrganizationInvitationForbidden() *CreateOrganizationInvitationForbidden {
	return &CreateOrganizationInvitationForbidden{}
}

/*CreateOrganizationInvitationForbidden handles this case with default header values.

forbidden
*/
type CreateOrganizationInvitationForbidden struct {
}

func (o *CreateOrganizationInvitationForbidden) Error() string {
	return fmt.Sprintf("[POST /organizations/{id}/invitations][%d] createOrganizationInvitationForbidden ", 403)
}

func (o *CreateOrganizationInvitationForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateOrganizationInvitationNotFound creates a CreateOrganizationInvitationNotFound with default headers values
func NewCreateOrganizationInvitationNotFound() *CreateOrganizationInvitationNotFound {
	return &CreateOrganizationInvitationNotFound{}
}

/*CreateOrganizationInvitationNotFound handles this case with default header values.

not found
*/
type CreateOrganizationInvitationNotFound struct {
}

func (o *CreateOrganizationInvitationNotFound) Error() string {
	return fmt.Sprintf("[POST /organizations/{id}/invitations][%d] createOrganizationInvitationNotFound ", 404)
}

func (o *CreateOrganizationInvitationNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCreateOrganizationInvitationUnprocessableEntity creates a CreateOrganizationInvitationUnprocessableEntity with default headers values
func NewCreateOrganizationInvitationUnprocessableEntity() *CreateOrganizationInvitationUnprocessableEntity {
	return &CreateOrganizationInvitationUnprocessableEntity{}
}

/*CreateOrganizationInvitationUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type CreateOrganizationInvitationUnprocessableEntity struct {
}

func (o *CreateOrganizationInvitationUnprocessableEntity) Error() string {
	return fmt.Sprintf("[POST /organizations/{id}/invitations][%d] createOrganizationInvitationUnprocessableEntity ", 422)
}

func (o *CreateOrganizationInvitationUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
