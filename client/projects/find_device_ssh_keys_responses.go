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

// FindDeviceSSHKeysReader is a Reader for the FindDeviceSSHKeys structure.
type FindDeviceSSHKeysReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *FindDeviceSSHKeysReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewFindDeviceSSHKeysOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 401:
		result := NewFindDeviceSSHKeysUnauthorized()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("response status code does not match any response statuses defined for this endpoint in the swagger spec", response, response.Code())
	}
}

// NewFindDeviceSSHKeysOK creates a FindDeviceSSHKeysOK with default headers values
func NewFindDeviceSSHKeysOK() *FindDeviceSSHKeysOK {
	return &FindDeviceSSHKeysOK{}
}

/*FindDeviceSSHKeysOK handles this case with default header values.

ok
*/
type FindDeviceSSHKeysOK struct {
	Payload *models.SSHKeyList
}

func (o *FindDeviceSSHKeysOK) Error() string {
	return fmt.Sprintf("[GET /devices/{id}/ssh-keys][%d] findDeviceSshKeysOK  %+v", 200, o.Payload)
}

func (o *FindDeviceSSHKeysOK) GetPayload() *models.SSHKeyList {
	return o.Payload
}

func (o *FindDeviceSSHKeysOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(models.SSHKeyList)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewFindDeviceSSHKeysUnauthorized creates a FindDeviceSSHKeysUnauthorized with default headers values
func NewFindDeviceSSHKeysUnauthorized() *FindDeviceSSHKeysUnauthorized {
	return &FindDeviceSSHKeysUnauthorized{}
}

/*FindDeviceSSHKeysUnauthorized handles this case with default header values.

unauthorized
*/
type FindDeviceSSHKeysUnauthorized struct {
}

func (o *FindDeviceSSHKeysUnauthorized) Error() string {
	return fmt.Sprintf("[GET /devices/{id}/ssh-keys][%d] findDeviceSshKeysUnauthorized ", 401)
}

func (o *FindDeviceSSHKeysUnauthorized) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}
