import jsPDF from 'jspdf';
import { getOrganizer } from '@/services/eventService';
import { type Profile } from '@/types/users';

export const gerarCertificado = async (
    nomeUsuario: string,
    nomeEvento: string,
    horasEvento: number,
    dataEvento1: string,
    dataEvento2: string,
    eventId: number,
) => {
    try {
        // Obtendo informações do organizador
        const response = await getOrganizer(eventId);
        const organizer: Profile = response.data;

        // Verificando se o organizador foi encontrado
        if (!organizer) {
            throw new Error('Organizador não encontrado');
        }

        const doc = new jsPDF();

        // Definindo o título do certificado
        doc.setFontSize(22);
        doc.text('Certificado de Participação', 105, 30, { align: 'center' });

        // Adicionando texto do certificado
        doc.setFontSize(16);
        doc.text(
            `Certificamos que ${nomeUsuario} participou do evento ${nomeEvento}`,
            20,
            60
        );
        doc.text(
            `com duração de ${horasEvento} horas, realizado entre os dias ${dataEvento1} e ${dataEvento2}.`,
            20,
            75
        );

        // Assinatura
        doc.text(`${organizer.name}`, 105, 130, { align: 'center' });
        doc.text('Organizador do Evento', 105, 140, { align: 'center' });

        // Nome do arquivo
        const nomeArquivo = `Certificado_${nomeUsuario.replace(/\s+/g, '_')}.pdf`;

        // Gerando o PDF e fazendo download
        doc.save(nomeArquivo);
    } catch (error) {
        console.error('Erro ao gerar o certificado:', error);
        throw error;
    }
};
