export interface Paciente {
  id?: number;
  nombre: string;
  apellido: string;
  fecha_nacimiento?: string;
  genero?: string;
  documento_identidad: string;
  telefono?: string;
  email?: string;
  direccion?: string;
  tipo_sangre?: string;
  fecha_registro?: string;
}
