// Code generated by go-swagger; DO NOT EDIT.

package userdata

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"
)

// ValidateUserdataReader is a Reader for the ValidateUserdata structure.
type ValidateUserdataReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *ValidateUserdataReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 204:
		result := NewValidateUserdataNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewValidateUserdataUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 422:
		result := NewValidateUserdataUnprocessableEntity()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewValidateUserdataNoContent creates a ValidateUserdataNoContent with default headers values
func NewValidateUserdataNoContent() *ValidateUserdataNoContent {
	return &ValidateUserdataNoContent{}
}

/*ValidateUserdataNoContent handles this case with default header values.

no content
*/
type ValidateUserdataNoContent struct {
}

func (o *ValidateUserdataNoContent) Error() string {
	return fmt.Sprintf("[POST /userdata/validate][%d] validateUserdataNoContent ", 204)
}

func (o *ValidateUserdataNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewValidateUserdataUnauthorized creates a ValidateUserdataUnauthorized with default headers values
func NewValidateUserdataUnauthorized() *ValidateUserdataUnauthorized {
	return &ValidateUserdataUnauthorized{}
}

/*ValidateUserdataUnauthorized handles this case with default header values.

unauthorized
*/
type ValidateUserdataUnauthorized struct {
}

func (o *ValidateUserdataUnauthorized) Error() string {
	return fmt.Sprintf("[POST /userdata/validate][%d] validateUserdataUnauthorized ", 401)
}

func (o *ValidateUserdataUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewValidateUserdataUnprocessableEntity creates a ValidateUserdataUnprocessableEntity with default headers values
func NewValidateUserdataUnprocessableEntity() *ValidateUserdataUnprocessableEntity {
	return &ValidateUserdataUnprocessableEntity{}
}

/*ValidateUserdataUnprocessableEntity handles this case with default header values.

unprocessable entity
*/
type ValidateUserdataUnprocessableEntity struct {
}

func (o *ValidateUserdataUnprocessableEntity) Error() string {
	return fmt.Sprintf("[POST /userdata/validate][%d] validateUserdataUnprocessableEntity ", 422)
}

func (o *ValidateUserdataUnprocessableEntity) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
