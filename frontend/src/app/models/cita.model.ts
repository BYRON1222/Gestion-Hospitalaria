export interface Cita {
  id?: number;
  paciente_id: number;
  medico_id: number;
  fecha_hora: string;
  motivo?: string;
  estado?: string;
}
