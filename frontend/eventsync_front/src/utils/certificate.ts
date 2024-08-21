import jsPDF from 'jspdf';

export const gerarCertificado = (
    nomeUsuario: string,
    nomeEvento: string,
    horasEvento: number,
    dataEvento1: string,
    dataEvento2: string,
    nomeOrg: string,
) => {
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
    doc.text(`${nomeOrg}`, 105, 130, { align: 'center' });
    doc.text('Nome do Organizador', 105, 140, { align: 'center' });

    // Nome do arquivo
    const nomeArquivo = `Certificado_${nomeUsuario.replace(/\s+/g, '_')}.pdf`;

    // Gerando o PDF e fazendo download
    doc.save(nomeArquivo);
};
