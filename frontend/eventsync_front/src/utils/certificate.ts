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

        // Configurando o documento para modo horizontal
        const doc = new jsPDF({ orientation: 'landscape' });

        // Definindo a fonte como Arial
        doc.setFont('Arial');

        // Desenhando as bordas verdes e azuis
        doc.setLineWidth(10); 
        doc.setDrawColor(129, 201, 250); // Cor #81c9fa
        doc.line(10, 10, 287, 10); // Borda azul superior
        doc.line(10, 200, 287, 200); // Borda azul inferior

        doc.setLineWidth(5);
        doc.setDrawColor(128, 231, 171); // Cor #80E7AB
        doc.line(15, 15, 282, 15); // Borda verde superior
        doc.line(15, 195, 282, 195); // Borda verde inferior

        // Definindo o título do certificado em negrito e com tamanho maior
        doc.setFontSize(18);
        doc.setFont('Arial', 'bold');
        doc.text('Certificado de Participação', 148.5, 50, { align: 'center' });

        // Adicionando texto do certificado
        doc.setFontSize(14);
        doc.setFont('Arial', 'normal');
        doc.text(
            `Certificamos que ${nomeUsuario} participou do evento ${nomeEvento}`,
            148.5,
            90,
            { align: 'center' }
        );
        doc.text(
            `com duração de ${horasEvento} horas, realizado entre os dias ${dataEvento1} e ${dataEvento2}.`,
            148.5,
            105,
            { align: 'center' }
        );

        // Assinatura
        doc.text(`${organizer.name}`, 148.5, 150, { align: 'center' });
        doc.text('Organizador do Evento', 148.5, 160, { align: 'center' });

        // Nome do arquivo
        const nomeArquivo = `Certificado_${nomeUsuario.replace(/\s+/g, '_')}.pdf`;

        // Gerando o PDF e fazendo download
        doc.save(nomeArquivo);
    } catch (error) {
        console.error('Erro ao gerar o certificado:', error);
        throw error;
    }
};
